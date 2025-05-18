from flask import Flask, request, jsonify, send_file
import config

app = Flask(__name__)

from app import routes