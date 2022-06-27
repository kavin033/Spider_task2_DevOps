import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
import subprocess as sp
file="/home/Spider_task2_DevOps/Server_kali"

app = Flask(__name__)
@app.route("/customers")
def kali_customers():
    out = sp.run(["php", file+"/kali_customers.php"], stdout=sp.PIPE)
    return out.stdout
@app.route("/headquarters")
def kali_headquarters():
    out = sp.run(["php", file+"/kali_headquarters.php"], stdout=sp.PIPE)
    return out.stdout
