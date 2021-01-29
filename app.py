import os
import json
import requests
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('NB2gli/J13truGWoTUHdV4RmtCdg+tQJMZilsy+gNDNKh9KqzBhoT1UJQ52uQ6io+WghT5VGLxkm6JdIlBKj9IJYD3ZEm1kGHn9smozXt76qS7nykV2dMhkdkQIzYB8EFemz7QilCcRp7m+C/wxBBQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5df4343c59b0042430e222166581c987')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    Awada=f"{message}"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=f"{Awada}"))




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
