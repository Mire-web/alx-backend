#!/usr/bin/env python3

from flask import Flask, render_templete

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_templete("0-index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
