from flask import Flask, request, jsonify, make_response
from dotenv import load_dotenv
from flask_cors import CORS
import json
import os
from naturify_agents import initialize_agent_with_new_openai_functions
from naturify_tools import music_player_tools

agent = initialize_agent_with_new_openai_functions(
    tools=music_player_tools)

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
access_token = os.environ.get('ACCESS_TOKEN')

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/query', methods=['POST'])
def query():
    data = request.get_data()
    print("Here: ", data)
    json_string = data.decode('utf-8')
    data_dict = json.loads(json_string)
    access_token = data_dict['accessToken']
    search_query = data_dict['queryString']
    result = agent({"input": "access_token: " + access_token + ", query: " + search_query})
    print(result)

    if isinstance(result["output"], str):
        message = "I'm sorry, but I couldn't understand your request. Can you please provide more information or clarify your query?"
        function = "not_called"
        status = 500
        return make_response(jsonify({'message': message, 'query': search_query, 'function': function}), status)
    message = result["output"]["message"]
    function = result["output"]["function"]
    status = result["output"]["status"]
    return make_response(jsonify({'message': message, 'query': search_query, 'function': function}), status)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)