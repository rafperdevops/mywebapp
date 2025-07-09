from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h2>Welcome</h2>
    <img src="https://png.pngtree.com/thumb_back/fh260/background/20230521/pngtree-sunflower-full-screen-backdrop-widescreen-photos-image_2684387.jpg" />
"""

@app.route("/saludos")
def saludos():
    return "<h1>Hola mundo!!!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)