
from flask_app import app, render_template, session, redirect, request
import random

@app.route('/games')
def index():
    random_number = random.randint(1, 100)  # random number between 1-100
    print(random_number)
    session['random_number'] = random_number
    session['attemps'] = 0
    return render_template('games/index.html')


@app.route('/guess', methods=['post'])
def process_guess():
    print(request.form)
    session['input_num'] = int(request.form['input_num'])
    print(session)
    return redirect("/games/guess")


@app.route("/games/guess")
def find_number():
    session['attemps'] += 1
    hint = ""
    if session['attemps'] >= 5 and session['input_num'] != session['random_number']:
        hint = "Sorry, Game Over!!"
        return render_template('games/guess.html', hint=hint)
    
    elif session['input_num'] == session['random_number']:
        hint = "You got it!!!"

    elif  session['input_num'] in range(session['random_number']-2, session['random_number']+3):
        hint = "Your number is so close"

    else:
        if session['input_num'] < session['random_number']:
            hint = "Your number is too low"

        if session['input_num'] > session['random_number']:
            hint = "Your number is too High"

    return render_template('games/guess.html', hint=hint)


@app.route("/reset")
def reset_game():
    session.clear()
    return redirect("/games")