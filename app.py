from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
import time
import ollama
import json

app = Flask(__name__)
CORS(app)

# These are defaults. Models are selected by looking at ollama list.
MODEL_1 = "llama3.2:latest"
MODEL_2 = "llama3.2:latest"
DEFAULT_SYSTEM_PROMPT = "Limit your output to 20 words. Use a conversational, interrogative style. Don't repeat yourself. Don't immediately answer a question with another question."

def get_llm_response(prompt, model, system_prompt):
    try:
        response = ollama.chat(model=model, messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

def stream_llm_responses(user_input, model1, model2, system_prompt1, system_prompt2):
    if not system_prompt1:
        system_prompt1 = DEFAULT_SYSTEM_PROMPT
    if not system_prompt2:
        system_prompt2 = DEFAULT_SYSTEM_PROMPT
    
    response1 = get_llm_response(user_input, model1, system_prompt1)
    yield json.dumps({'response1': f"{model1} says: {response1}"})
    
    response2 = get_llm_response(user_input, model2, system_prompt2)
    yield json.dumps({'response2': f"{model2} says: {response2}"})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('user_input')
    model1 = data.get('model1')
    model2 = data.get('model2')
    system_prompt1 = data.get('system_prompt1')
    system_prompt2 = data.get('system_prompt2')
    
    return Response(stream_llm_responses(user_input, model1, model2, system_prompt1, system_prompt2), mimetype='application/json')

@app.route('/models', methods=['GET'])
def list_models():
    try:
        models = ollama.list()
        return jsonify({'models': [model['model'] for model in models['models']]})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/clear', methods=['POST'])
def clear():
    # Placeholder for clearing conversation history
    return jsonify({'message': 'Conversation cleared'})

@app.route('/stop', methods=['POST'])
def stop():
    return jsonify({'message': 'Chat stopped'})

@app.route('/default_system_prompt', methods=['GET'])
def default_system_prompt():
    return jsonify({'default_system_prompt': DEFAULT_SYSTEM_PROMPT})

if __name__ == '__main__':
    app.run(debug=True)
