import os
import socket
from math import sqrt

from flask import Flask, request


def squareroot(n=None):
    if n is None:
        return "Empty input"
    try:
        number = float(n)
    except ValueError:
        return "Not a numerical value"
    else:
        if number >= 0:
            return "Square Root of {} is {}".format(number, sqrt(number))
        else:
            return "Negative numbers don't have real square roots"


def create_app():
    app = Flask(__name__)
    # Use the following url to get the result replicing <IP>
    # with the external IP, for example,
    # http://http://20.76.191.125:5000/

    @app.route("/")
    def hello_world():
        # to get the hostname
        host = socket.gethostname()
        # to get the host ip
        ip = socket.gethostbyname(host)
        message = os.getenv("MESSAGE", "Flask Demo")
        return "{} on host {} ({})".format(message, host, ip)

    # Use the following url to get the result replicing <IP>
    # with the external IP, for example,
    # http://http://20.76.191.125:5000/root_number?number=2
    @app.route("/squareroot_number")
    def sqareroot_number():
        return squareroot(request.args.get("number"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
