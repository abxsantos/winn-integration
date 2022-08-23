# Installation

Create a python venv and install the requirements with `pip install -r requirements.txt`

Install [ngrok](https://ngrok.com/download)

Run the flask app with `flask --app api/server.py:app run`

Expose the 5000 port with ngrok, thus allowing to receive a callback with `ngrok http 5000`