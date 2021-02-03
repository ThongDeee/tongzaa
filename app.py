#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Server Side
from flask import Flask
from flask.views import MethodView
import requests
import os

app = Flask(__name__)


def getbotnoi(self,name):
    undefined=name
    url = f"https://openapi.botnoi.ai/botnoi/ecommerce?keyword={undefined}"   
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTIwOTM5MjcsImlkIjoiNTJjYTJjODgtNDI2Ny00ZDEwLTkwNzktYmE4MGMxZWNhMzQ5IiwiaXNzIjoiZnloRHFJV1Npb3R4YmN3MkI4amZ5dUJBdUNHdFRLcm4iLCJuYW1lIjoiMTQzMy4wOCIsInBpYyI6Imh0dHBzOi8vcHJvZmlsZS5saW5lLXNjZG4ubmV0LzBoR1diUjVwYTVHSGhmS3pCcDdReG5MMk51RmhVb0JSNHdKMGxXR0h3dlFFMTJIVjRvWVJoVlNuOV9RMHh4SFZncE1VNEhHM3A1UWgxdyJ9.wfEGlqTBL1YQMsKWOEunptFk3mudSINF0ohdjTraCD0'}
    response = requests.request("Get", url, headers=headers).json()
    return response


class WeatherCity(MethodView):
    def get(self, name):
        return getbotnoi(self, name)


app.add_url_rule("/w/<string:name>", view_func=WeatherCity.as_view("weather"))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
