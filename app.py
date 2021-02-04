from flask import Flask
from flask_restful import Api,Resource,abort,reqparse,marshal_with,fields
import json
import requests
import os

app=Flask(__name__)
api=Api(app)

##input  
def getbotnoi(self,inp1):
    undefined=inp1
    url = f"https://openapi.botnoi.ai/service-api/botnoichitchat?keyword={undefined}&styleid=6&botname=โอม"   
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTI2OTk2NDEsImlkIjoiNTJjYTJjODgtNDI2Ny00ZDEwLTkwNzktYmE4MGMxZWNhMzQ5IiwiaXNzIjoiZnloRHFJV1Npb3R4YmN3MkI4amZ5dUJBdUNHdFRLcm4iLCJuYW1lIjoiMTQzMy4wOCIsInBpYyI6Imh0dHBzOi8vcHJvZmlsZS5saW5lLXNjZG4ubmV0LzBoR1diUjVwYTVHSGhmS3pCcDdReG5MMk51RmhVb0JSNHdKMGxXR0h3dlFFMTJIVjRvWVJoVlNuOV9RMHh4SFZncE1VNEhHM3A1UWgxdyJ9.9cjAyRzuUG7NHDpoCxieFVwPsvpUpJLRx5wQ1o0l7P8'}
    response = requests.request("Get", url, headers=headers).json()
    return response

#design
@app.route('/')
def index():
    return "hello"

class speak(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('input', type=str)
        dictp = parser.parse_args()
        inp1 = dictp['input']
        
        result = getbotnoi(self,inp1)
        
        return result
   
#call
api.add_resource(speak,'/cal',endpoint='cal')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
