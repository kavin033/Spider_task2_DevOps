import os
from flask import Flask
import json
import subprocess as sp
file="/home/kavin/task2/Server_debian"

app = Flask(__name__)
@app.route("/customers")
def kali_customers():
    out = sp.run(["php", file+"/debian_customers.php"], stdout=sp.PIPE)
    return out.stdout
@app.route("/headquarters")
def kali_headquarters():
    out = sp.run(["php", file+"/debian_headquarters.php"], stdout=sp.PIPE)
    return out.stdout
