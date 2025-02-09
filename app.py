from flask import Flask, render_template

app = Flask(__name__)

@app.route('/games')
def games():

# Данные об играх (пока временно в коде, потом можно перенести в базу данных)

 games_data = [

    {"title": "The Witcher 3", "genre": "RPG", "price": 600, "release_year": 2015, "rating": 4.9, "image_url": "https://image.api.playstation.com/vulcan/ap/rnd/202211/0711/kh4MUIuMmHlktOHar3lVl6rY.png"},
    {"title": "Cyberpunk 2077", "genre": "RPG", "price": 1200, "release_year": 2020, "rating": 4.2, "image_url": "https://th.bing.com/th/id/R.f254a8e449d9adc25fa91d644fb31e1b?rik=WV9J7dhT31QbMw&pid=ImgRaw&r=0"},
    {"title": "S.T.A.L.K.E.R. 2", "genre": "Shooter", "price": 1400, "release_year": 2024, "rating": 4.7, "image_url": "https://gamefaqs.gamespot.com/a/box/6/2/7/803627_front.jpg"},
    {"title": "Doom Eternal", "genre": "Shooter", "price": 900, "release_year": 2020, "rating": 4.8, "image_url": "https://www.geeky-gadgets.com/wp-content/uploads/2020/12/DOOM-Eternal-Xbox.jpg"},
    {"title": "Dark Souls III", "genre": "RPG", "price": 700, "release_year": 2016, "rating": 4.8, "image_url": "https://cdn.mobygames.com/covers/3314757-dark-souls-iii-playstation-4-front-cover.jpg"},
    {"title": "Hollow Knight", "genre": "Adventure", "price": 500, "release_year": 2017, "rating": 4.9, "image_url": "https://f4.bcbits.com/img/a0907743342_10.jpg"},
    {"title": "Elden Ring", "genre": "RPG", "price": 1300, "release_year": 2022, "rating": 4.9, "image_url": "https://th.bing.com/th/id/R.08c34c1059e0da6633eb126ddafb4fb0?rik=Wvha2tNI2VVTRA&pid=ImgRaw&r=0"},
    {"title": "Dying Light 2", "genre": "Action", "price": 1100, "release_year": 2022, "rating": 4.1, "image_url": "https://tsdcovers.files.wordpress.com/2022/02/dying-light.jpg?w=1500"}
 
 ]

 return render_template('games.html', games=games_data)
 

@app.route('/new_releases')
def new_releases():
    current_year = 2024  # Берём текущий год
    new_games = [game for game in games_data if game["release_year"] >= current_year - 2]  # Игры за последние два года
    return render_template('games.html', games=new_games)

@app.route('/classic')
def classic():
    current_year = 2024  # Текущий год
    classic_games = [game for game in games_data if game["release_year"] <= current_year - 5]  # Игры старше 5 лет
    return render_template('games.html', games=classic_games)

@app.route('/popular')
def popular():
    popular_games = [game for game in games_data if game.get("rating", 0) >= 4.5]  # Игры с рейтингом выше 4.5
    return render_template('games.html', games=popular_games)

@app.route("/")
def home():
        return "Welcome to Igroman"

if __name__ == '__main__':
    app.run(debug=True)