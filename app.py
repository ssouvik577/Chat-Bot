from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up your OpenAI API credentials
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
@app.route('/chat', methods=['POST'])
def chat():
    condition = request.form['condition']
    severity = request.form['severity']
    message = request.form['message']

    # Define the prompt based on the selected condition, severity, and user message
    prompt = f"Health condition: {condition}\nSeverity: {severity}\nUser: {message}"

    # Generate a response from the ChatGPT API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,  # Adjust the number of tokens as needed
        n=1,
        stop=None,
        temperature=0.7
    )

    reply = response.choices[0].text.strip()

    return reply

if __name__ == '__main__':
    app.run(debug=True)
