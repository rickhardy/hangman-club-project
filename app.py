# User playing hangman in their browser"
# Relationship to routes_py => Sends HTTP requests to, HTTP/HTTPS"
# Relationship from routes_py - recieves feedback for the user and displays it"

from flask import Flask, request, redirect, url_for, render_template, session
#from hangman_code.start_game import load_game
#from hangman_code.play_game_functions import play_game
from hangman_code.game import Game
from hangman_code.word_selection import choose_word

import string


app = Flask(__name__)
app.secret_key = "super-secret-key-change-this"


# This is the home page. It has a selection of new game, resume game,
# Factory reset or exit game.
#The Start_game_selection function will return the game object with the correct
# Data in it for its selection
@app.route("/", methods=["GET", "POST"])
def index():
    session.clear()
    if request.method == "POST":
        selection = request.form.get("action")
        word = choose_word()
        game = Game(word=word) 
        session["game"] = game.to_dict()
        return render_template("playing_game.html", game=session["game"],alphabet=string.ascii_uppercase)
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():

    #game = session["game"]
    game = Game(
        word=session["game"]["word"],
        used_letters=session["game"]["used_letters"],
        letters_remaining=session["game"]["letters_remaining"]
    )
    
    
    # Get the letter from the form / user
    letter = request.form.get("letter")
    
    game.make_guess (letter=letter)
    session["game"] = game.to_dict()

    

    #word_attempt = request.form.get("word_attempt")
    #if not word_attempt:
        #word_attempt = ""
    # Send the letter to the programme to make the guess
    #game = play_game(game, letter, word_attempt)
    # TO BE DONE BY GUESSED_LETTERS_AND_WORDS
    # Normalize to uppercase (your letters list is A–Z)
    #letter = letter.upper()
    return render_template("playing_game.html", game=session["game"], alphabet=string.ascii_uppercase)


@app.route("/name_game", methods=["POST"])
def name_game():
    
    current_game = session["game"]

    # 1. Read the name from the form
    game_name = request.form.get("game_name").strip()

    # 2. Add the game name to the local game object

    current_game["game_name"] = game_name

    #3. Update the current_game_status to in play
    current_game["current_game_status"] = 1

    # 4. Store updated object back into session
    session["game"] = current_game
    print ('in name game:', session["game"]["game_name"])

    # 5. Back to the main page
    return render_template("playing_game.html", game=session["game"], alphabet=string.ascii_uppercase)


@app.route("/reset", methods=["POST"])
def reset():
    return redirect("/")

@app.route("/show_line", methods=["POST"])
def show_line():
    print('Hello')
    return redirect(url_for("index"))

@app.route("/closed", methods=["POST"])
def closed():
    selection = request.form.get("action")
    print(f"This is the selection : {selection}")
    #session["game"] = load_game(selection)
    return render_template("closed.html")

if __name__ == '__main__':
    app.run(debug=True)



