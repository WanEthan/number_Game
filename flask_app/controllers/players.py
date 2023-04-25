
from flask_app import app, render_template, redirect, request, session
from flask_app.models.player import Player


@app.route("/")
def home():
    return render_template("index.html")

#! CREATE


@app.route('/create', methods=['post'])
def new_player_data():
    print(request.form)
    session['name'] = request.form['name']
    Player.add_new_player(session)
    return redirect("/show")

#! Read All Players


@app.route("/show")
def read_all_players():
    players = Player.get_all_player()
    print(players)
    return render_template("show.html", players=players)


#! Just allow user to go back to the home page
@app.route("/back")
def go_back():
    return redirect("/")
