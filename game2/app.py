from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, jsonify, request
from collections import defaultdict


app = Flask(__name__)
app.secret_key = 'crazyprince'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Videogames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    playtime = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comments = db.Column(db.String(1000), nullable=True)


with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    videoigre = Videogames.query.all()
    videoigre = [v.__dict__ for v in videoigre]
    return render_template('index.html', videoigre=videoigre)  

@app.route('/data')
def data():
    games = Videogames.query.all()
    playtime_per_platform = defaultdict(float)
    for game in games:
        playtime_per_platform[game.platform] += game.playtime

    data = [{'label': platform, 'value': playtime} for platform, playtime in playtime_per_platform.items()]
    return jsonify(data)

@app.route('/data2')
def data2():
    games = Videogames.query.all()

    playtime_per_genre = defaultdict(float)
    for game in games:
        playtime_per_genre[game.genre] += game.playtime

    data = [{'label': genre, 'value': playtime} for genre, playtime in playtime_per_genre.items()]
    return jsonify(data)

@app.route('/data3')
def data3():
    games = Videogames.query.all()
    rating_per_platform = defaultdict(list)
    for game in games:
        rating_per_platform[game.platform].append(game.rating)

    average_rating_per_platform = {platform: sum(ratings) / len(ratings) for platform, ratings in rating_per_platform.items()}

  
    data = [{'label': platform, 'value': avg_rating} for platform, avg_rating in average_rating_per_platform.items()]
    return jsonify(data)

@app.route('/data4')
def data4():
    games = Videogames.query.all()

    games_per_genre = defaultdict(int)
    for game in games:
        games_per_genre[game.genre] += 1

    data = [{'label': genre, 'value': count} for genre, count in games_per_genre.items()]
    return jsonify(data)



@app.route("/stats")
def stats():
    return render_template("statistics.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/addgame", methods=["POST"])
def add():
    name = request.form["name"]
    platform = request.form["platform"]
    genre = request.form["genre"]
    playtime = request.form["playtime"]
    rating = request.form["rating"]
    comments = request.form["comments"]

    new_videogame = Videogames(name=name, platform=platform, genre=genre, playtime=playtime, rating=rating, comments=comments)
    db.session.add(new_videogame)
    db.session.commit()

    return redirect(url_for("home"))

@app.route('/delete-game', methods=['POST'])
def delete_game():
    game_id = request.json['gameId']
    
    # Implement your delete game logic here
    game = Videogames.query.get(game_id)
    if game:
        db.session.delete(game)
        db.session.commit()
        return jsonify({'success': True, })
    else:
        return jsonify({'success': False, 'message': 'Game not found'})



if __name__ == "__main__":
    app.run(debug=True)

               

                