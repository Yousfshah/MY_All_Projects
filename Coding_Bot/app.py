from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')
        
        # OpenRouter API request
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {os.getenv("OPENROUTER_API_KEY")}',
                'Content-Type': 'application/json',
                'HTTP-Referer': request.headers.get('Origin', '*'),
                'X-Title': 'SQLGenius'
            },
            json={
                'model': 'qwen/qwen2.5-vl-72b-instruct:free',
                'messages': [
                    {
                        'role': 'system',
                        'content': 'You are an expert in SQL query optimization. Format your responses in this structure:\n\n# Query Purpose\n[Brief description of what the query does]\n\n## SQL Query\n```sql\n[Your optimized SQL query here]\n```\n\n## Explanation\n[Detailed explanation with markdown formatting using:\n- Bullet points for key aspects\n- **Bold** for important terms\n- Headers for different sections]\n\n## Optimization Notes\n- List performance considerations\n- Explain why certain approaches were chosen'
                    },
                    {
                        'role': 'user',
                        'content': user_message
                    }
                ]
            }
        )
        
        if response.status_code != 200:
            return jsonify({'error': 'API request failed'}), 500
            
        data = response.json()
        return jsonify({'response': data['choices'][0]['message']['content']})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Sorry, I encountered an error. Please try again.'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
