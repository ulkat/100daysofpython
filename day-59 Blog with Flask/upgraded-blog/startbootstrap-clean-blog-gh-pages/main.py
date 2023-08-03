from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/e0e19da732af6138bef6")
all_blogs = response.json()


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_blogs=all_blogs)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:blog_id>")
def post(blog_id):
    for blog in all_blogs:
        if blog["id"] == blog_id:
            requested_blog = blog
    return render_template("post.html", blog=requested_blog)

if __name__ == "__main__":
    app.run(debug=True)