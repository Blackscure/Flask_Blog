from flask import Flask,render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Blacks Cure',
        'title': 'Blog Post1',
        'date_posted': 'october 20, 2018'
    },
    {
        'author': 'Ney neema',
        'title': 'Blog Post2',
        'date_posted': 'october 7, 2018'
    }
]



@app.route("/")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

if __name__ == "__main__":
    app.run(debug=True)