from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Time App!"

@app.route('/time')
def get_time():
    # Return the current date and time as a string
    return f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
