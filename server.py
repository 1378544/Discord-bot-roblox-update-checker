from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

def run_server():
    app.run(host='0.0.0.0', port=8080)
