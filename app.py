from flask import Flask, session, render_template
from boggle import Boggle
from boggle import make_board
app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"

boggle_game = Boggle()

@app.route("/")
def display_Board():
    """Create and display board in session."""
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board=board)

# https://hackersandslackers.com/flask-jinja-templates/
# https://www.geeksforgeeks.org/templating-with-jinja2-in-flask/



   