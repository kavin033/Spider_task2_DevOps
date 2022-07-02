import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
import subprocess as sp
file="/home/Spider_task2_DevOps/Server_secrets"

app = Flask(__name__)
@app.route("/secrets")
def kali_customers():
    out = sp.run(["php", file+"/secrets.php"], stdout=sp.PIPE)
    return out.stdout
