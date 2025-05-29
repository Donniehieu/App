from flask import Flask
from routes.horoscope import horoscope_bp

app = Flask(__name__)
app.register_blueprint(horoscope_bp)

if __name__ == '__main__':
    app.run(debug=True)