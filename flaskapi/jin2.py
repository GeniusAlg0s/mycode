#!/usr/bin/env python3
from flask import Flask
from flask import session
from flask import Flask, render_template
from flask import redirect
from flask import url_for
from flask import request


app = Flask(__name__)

app.secret_key = "any random string"
groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/")
def index():

    return render_template("jinchal.html", ip = groups[0]['ip'], fqdn = groups[0]['fqdn'],  hostname =groups[0]['hostname'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

