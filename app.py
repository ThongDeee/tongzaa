import os
import json
import time
import requests
from flask import Flask, request, abort
from flask_jsonpify import jsonpify
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

@app.route('/')

class botnoi(Resource):
    def get(self):
        parser = reparse.RequestParser()
        parser.add_argument('keyword', type=str)
        dictp = parser.parse_args()
        key=keyword['keyword']
    Awada = (event.message.text)
    def getbotnoi(Awada):
        url = f"https://openapi.botnoi.ai/botnoi/ecommerce?keyword={Awada}" 
        headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTIwOTM5MjcsImlkIjoiNTJjYTJjODgtNDI2Ny00ZDEwLTkwNzktYmE4MGMxZWNhMzQ5IiwiaXNzIjoiZnloRHFJV1Npb3R4YmN3MkI4amZ5dUJBdUNHdFRLcm4iLCJuYW1lIjoiMTQzMy4wOCIsInBpYyI6Imh0dHBzOi8vcHJvZmlsZS5saW5lLXNjZG4ubmV0LzBoR1diUjVwYTVHSGhmS3pCcDdReG5MMk51RmhVb0JSNHdKMGxXR0h3dlFFMTJIVjRvWVJoVlNuOV9RMHh4SFZncE1VNEhHM3A1UWgxdyJ9.wfEGlqTBL1YQMsKWOEunptFk3mudSINF0ohdjTraCD0'
}
        response = requests.request("Get", url, headers=headers).json()
        if response['intent'] ==  "ขอเวลาปิดทำการ":
            return "ไม่มีวันปิดครับ"
        else: 
            return "ไม่เข้าใจคำถาม"
    Bunny = getbotnoi(Awada)


@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    Awada = (event.message.text)
    def getbotnoi(Awada):
        url = f"https://openapi.botnoi.ai/botnoi/ecommerce?keyword={Awada}" 
        headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTIwOTM5MjcsImlkIjoiNTJjYTJjODgtNDI2Ny00ZDEwLTkwNzktYmE4MGMxZWNhMzQ5IiwiaXNzIjoiZnloRHFJV1Npb3R4YmN3MkI4amZ5dUJBdUNHdFRLcm4iLCJuYW1lIjoiMTQzMy4wOCIsInBpYyI6Imh0dHBzOi8vcHJvZmlsZS5saW5lLXNjZG4ubmV0LzBoR1diUjVwYTVHSGhmS3pCcDdReG5MMk51RmhVb0JSNHdKMGxXR0h3dlFFMTJIVjRvWVJoVlNuOV9RMHh4SFZncE1VNEhHM3A1UWgxdyJ9.wfEGlqTBL1YQMsKWOEunptFk3mudSINF0ohdjTraCD0'
}
        response = requests.request("Get", url, headers=headers).json()
        if response['intent'] ==  "ขอเวลาปิดทำการ":
            return "ไม่มีวันปิดครับ"
        else: 
            return "ไม่เข้าใจคำถาม"
    Bunny = getbotnoi(Awada)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=f"{Bunny}"))




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
