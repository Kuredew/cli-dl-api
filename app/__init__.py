from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import config

app = Flask(__name__)
CORS(app)

from app import routes