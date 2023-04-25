from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
# our index route will handle rendering our form
# set a secret key for security purposes
app.secret_key = 'keep secret and keep safe'
