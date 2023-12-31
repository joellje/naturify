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
    print(request)
    data = request.get_data()
    json_string = data.decode('utf-8')
    data_dict = json.loads(json_string)
    access_token = data_dict['accessToken']
    search_query = data_dict['queryString']
    
    result = agent({"input": access_token + search_query})
    answer = result["output"]
    return make_response(jsonify({'result': answer}), 200) #TODO: tidy responses

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)

# while True:
#     request = input(
#         "\n\nRequest: ")
#     result = agent({"input": access_token + request})
#     answer = result["output"]
#     print(answer)