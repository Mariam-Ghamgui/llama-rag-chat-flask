# llama2-rag-chat Frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Description
This is the frontend for the llama2-rag-chat project. It's built with Vue.js and provides a user-friendly interface for interacting with the ENETCOM chatbot powered by the llama2 model.

## Features
- Chatbot widget that can be toggled open and closed
- Initial greeting message when the chat is opened
- User and bot message display with avatars
- Input field for user questions
- Clear chat functionality
- Responsive design

## Components
- `App.vue`: The main component that includes the chat widget and handles the chat logic

## API Integration
The frontend communicates with the Flask backend API, which uses the llama2 model for natural language processing. Ensure that the backend server is running and the API endpoint in `App.vue` is correctly set to your backend URL (default is `http://localhost:5000/api/chat`).

## Customization
- Bot and user avatars can be customized by replacing the image files in the `src/assets` directory
- Colors and styles can be adjusted in the `<style>` section of `App.vue`

## Note
This frontend is designed to work with the corresponding Flask backend using the llama2 model. Make sure the backend is properly set up and running before using this frontend.

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
