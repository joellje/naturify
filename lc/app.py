from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import json
import os
import spotipy
from naturify_agents import initialize_agent_with_new_openai_functions
from naturify_tools import music_player_tools

agent = initialize_agent_with_new_openai_functions(
    tools=music_player_tools)

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def hello():
#     return '<h1>Hello, World!</h1>'

# @app.route('/query', methods=['POST'])
# def query():
#     data = request.get_data()
#     json_string = data.decode('utf-8')
#     data_dict = json.loads(json_string)
#     access_token = data_dict['accessToken']
#     search_query = data_dict['queryString']
    
#     result = agent({"input": {"access_token": access_token, "search_query": search_query}})
#     answer = result["output"]
#     return answer


# if __name__ == '__main__':
#     app.run(debug=True, host='localhost', port=8080)

while True:
    request = input(
        "\n\nRequest: ")
    access_token = "BQD-BkzVcGF9IRWo9gaeCdRzuta8D63MdLwlqh3mqnTzfeZSNUOuzowLF9f24HbyTEMzkIcpk1lro2uat-44iHsGCR0gHO28fsTegqOOTUTNg3UygZRXdOaSCj3mQLbnPJtOerf4ZlWvBF7_MMkKm39Ov4m8V6_JqnFN5p132f2oM-OUM_wJPzMNuNF_etbF8H_2KcJ1XiwhnZTr5y6lbhhzHY99Tg"
    result = agent({"input": access_token + request})
    answer = result["output"]
    print(answer)