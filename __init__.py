from flask import Flask
app = Flask(__name__)
from gopark import app
from flask import render_template, request, redirect
import gopark.main