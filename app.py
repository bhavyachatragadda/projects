from flask import Flask, request, jsonify
import openai  # Make sure to install the OpenAI library

app = Flask(__name__)

# Initialize OpenAI API (use your actual API key here)
openai.api_key = 'YOUR_API_KEY'

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    content_type = data['contentType']
    user_input = data['userInput']

    prompt = f"Generate a {content_type} about: {user_input}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or your preferred model
            messages=[{"role": "user", "content": prompt}]
        )
        generated_content = response['choices'][0]['message']['content']
        return jsonify({'generatedContent': generated_content})
    except Exception as e:
        return jsonify({'generatedContent': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
