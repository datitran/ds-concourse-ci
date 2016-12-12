import os
from model import power
from flask import Flask

app = Flask(__name__)

port = int(os.getenv("PORT", 9099))


@app.route("/")
def model():
    number = 2
    return "The square of {} is {}.".format(number, power(number))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
