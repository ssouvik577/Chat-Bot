# Chat-Bot
ChatBot using Flask
from flask import Flask, render_template, request: This line imports the necessary modules from the Flask library. Flask is a web framework for Python that simplifies web development.
import openai: This line imports the OpenAI library, which provides access to the OpenAI API for language models.
app = Flask(__name__): This line creates a Flask application instance.
openai.api_key = This line sets the OpenAI API key to authenticate and authorize API requests.
@app.route('/'): This line is a decorator that defines a route for the home page of the web app. It specifies that the following function (index()) should be called when the specified route is accessed.
def index():: This function handles the request for the home page. It renders the index.html template, which displays the chatbot helpdesk interface.
@app.route('/chat', methods=['POST']): This line is a decorator that defines a route for handling chat interactions. It specifies that the following function (chat()) should be called when the specified route with the POST method is accessed.
def chat():: This function handles the chat interaction. It retrieves the selected health condition, severity, and user message from the form data submitted via the chat form. It then generates a prompt using this information and sends a request to the ChatGPT API using the OpenAI library. The response from the API is extracted and returned as the reply.
if __name__ == '__main__':: This conditional statement checks if the script is being run directly (not imported as a module). If true, it calls app.run() to start the Flask application.
app.run(debug=True): This line starts the Flask development server. The debug=True argument enables debug mode, providing detailed error messages. It's useful during development but should be disabled in a production environment.
Overall, this Python code sets up a Flask web app that serves as a chatbot helpdesk. It handles user interactions, retrieves user input, and sends requests to the ChatGPT API for generating responses. The OpenAI API key is used for authentication, and the Flask framework takes care of routing and rendering the HTML templates.
