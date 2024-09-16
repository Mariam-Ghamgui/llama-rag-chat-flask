# llama2-rag-chat-with-mysql-database

## Description
This project demonstrates a chatbot that can answer questions about ENETCOM using a MySQL database. It uses a Vue.js frontend, a Flask backend with the Ollama llama2 model, and a MySQL database.

## Project Structure
- `frontend/`: Vue.js frontend application
- `app.py`: Flask backend server
- `requirements.txt`: Python dependencies for the backend

## How to Clone and Run the Project Locally

### Prerequisites
- Python 3.8 or higher
- Node.js and npm
- MySQL database
- Ollama installed

### Cloning the Repository
1. Open your terminal
2. Run the following command:
   ```bash
   git clone https://github.com/yourusername/llama2-rag-chat-with-mysql-database.git
   cd llama2-rag-chat-with-mysql-database
   ```

### Backend Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your MySQL database and update the connection string in `app.py`

## Database Setup

1. Create the `rag_test` database:
   ```sql
   CREATE DATABASE rag_test;
   USE rag_test;
   ```

2. Import the `rag_test.sql` file:
   Exit the MySQL client if you're in it, then use the command line to import the SQL file:
   ```bash
   mysql -u your_username -p rag_test rag_test.sql
   ```
   Replace `your_username` with your MySQL username. 

3. Verify the import:
   Log back into MySQL and run:
   ```sql
   USE rag_test;
   SHOW TABLES;
   SELECT COUNT(*) FROM Track;
   ```

This process will create the `rag_test` database and populate it with all the tables and data from your SQL file.   

### Ollama Setup
1. Install Ollama if you haven't already:
   [Ollama Installation Guide](https://ollama.com/download)
2. Pull the llama2 model:
   ```bash
   ollama pull llama2
   ```   

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install the required npm packages:
   ```bash
   npm install
   ```

## Running the Application

### Start the Backend Server
From the root directory of the project:
```bash
python app.py
```

### Start the Frontend Development Server
From the `frontend` directory:
```bash
npm run serve
```
The application should now be running. Access the frontend through the URL provided by the Vue.js development server (typically `http://localhost:8080`).

## Usage
- Open the application in your web browser
- Click on the chatbot icon to open the chat interface
- Type your questions about ENETCOM in the chat input
- The chatbot will respond with information retrieved from the MySQL database

## Example Test Questions
To test the chatbot's functionality, you can try asking the following questions:

1. How many albums are there in the database?
2. Who are the top 5 artists with the most albums?
3. What is the total number of tracks in the database?
4. List the names of all genres available in the database.
5. How many customers are from Germany?
6. What is the average length of tracks in milliseconds?
7. How many playlists are there in the database?
8. List the top 5 countries with the most customers.
9. What is the total duration of all tracks by the artist "Queen"?
10. Which customer has the highest total purchase amount?

The application should now be running. Access the frontend through the URL provided by the Vue.js development server (typically `http://localhost:8080`).

## Usage
- Open the application in your web browser
- Click on the chatbot icon to open the chat interface
- Type your questions about

## Useful Links
- [Vue.js](https://vuejs.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Ollama](https://ollama.com/)
- [Langchain SQL](https://python.langchain.com/docs/use_cases/sql)
- [MySQL Connector Python](https://pypi.org/project/mysql-connector-python/)

## Note
Ensure that your MySQL database is properly set up and the connection details in `app.py` are correct before running the application.
