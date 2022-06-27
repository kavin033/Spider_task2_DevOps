import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
import html
import subprocess as sp
file="/home/Spider_task2_DevOps/Server_arch"

app = Flask(__name__)
@app.route("/customers")
def arch_customers():
    out = sp.run(["php", file+"/arch_customers.php"], stdout=sp.PIPE)
    return out.stdout
@app.route("/headquarters")
def arch_headquarters():
    out = sp.run(["php", file+"/arch_headquarters.php"], stdout=sp.PIPE)
    return out.stdout
