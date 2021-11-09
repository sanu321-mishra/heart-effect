from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def heart():
    return render_template("heart.html")


if __name__== "__main__":
    app.run(debug=True)    