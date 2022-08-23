from flask import Flask, request

app = Flask(__name__)


@app.post("/")
def winn_callback():
    app.logger.info("Received the request body: %s", request.json)
    return request.json
