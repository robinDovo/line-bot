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

line_bot_api = LineBotApi('7tm8hGdemeO/BygYoTgArVYVTdcmjEVCOEmkpFHraKSdFki8hfmBgcC6dNjT+okoLFtoNpn8MAP8pQQdwJhO4+fgVHOfjcOqmhxHNsDsjAgMa01SsnroXANMX1SawKtHviWFevN5uFbTBOpCLGnonAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f397ffce9a6475058fbe498506ae8cb6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '吃飽沒'
    if msg == 'hi':
        s = 'hi' 
    elif msg == '睡了沒':
        s = '還沒 '

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()