from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
import logging
from functools import lru_cache

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

def connectDatabase():
    try:
        mysql_uri = "mysql+mysqlconnector://root:root@localhost:3306/rag_test"
        db = SQLDatabase.from_uri(mysql_uri)
        logging.info("Database connected")
        tables = db.get_table_names()
        logging.info(f"Tables in the database: {tables}")
        return db
    except Exception as e:
        logging.error(f"Failed to connect to the database: {str(e)}")
        return None

@lru_cache(maxsize=128)  # Caching for repeated queries
def runQuery(db, query):
    if not query:
        return "No valid SQL query was generated."
    try:
        return db.run(query)
    except Exception as e:
        return f"An error occurred: {str(e)}"

def getDatabaseSchema(db):
    return db.get_table_info() if db else "Please connect to database"

llm = ChatOllama(model="llama2")

@lru_cache(maxsize=128)
def getQueryFromLLM(question, schema):
    template = """Below is the schema of MYSQL database, read the schema carefully about the table and column names. Also take care of table or column name case sensitivity.
    The available tables are: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, and Track.
    Finally answer user's question in the form of SQL query.

    {schema}

    Please only provide the SQL query and nothing else

    For example:
    question: how many albums we have in database
    SQL query: SELECT COUNT(*) FROM Album;
    question: how many customers are from Brazil in the database ?
    SQL query: SELECT COUNT(*) FROM Customer WHERE Country='Brazil';

    Your turn:
    question: {question}
    SQL query:
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "schema": schema
    })
    
    return extract_sql_query(response.content)

def extract_sql_query(text):
    keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP']
    for keyword in keywords:
        if keyword in text.upper():
            start = text.upper().index(keyword)
            query = text[start:].split(';')[0].strip() + ';'
            query = query.replace('User', 'Customer').replace('user', 'Customer')
            return query
    return ""

def getResponseForQueryResult(question, query, result):
    template = """
    Question: {question}
    SQL Query: {query}
    Result: {result}

    Please provide a concise and relevant response to the question based on the SQL query result.
    Response:
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "query": query,
        "result": result
    })

    return response.content

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    db = connectDatabase()
    if not db:
        return jsonify({"error": "Failed to connect to the database"}), 500

    schema = getDatabaseSchema(db)
    query = getQueryFromLLM(question, schema)
    result = runQuery(db, query)
    response = getResponseForQueryResult(question, query, result)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
