from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/time")
def get_current_time():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current time is: {now}"

if __name__ == "__main__":
    # Bind to all interfaces and listen on port 80
    app.run(host="0.0.0.0", port=80)
