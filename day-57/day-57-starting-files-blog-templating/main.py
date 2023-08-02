from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()

    return render_template("index.html", all_blogs=all_blogs)

# alltaki değişken direkt urlye girdiğin değişken!!
@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    for blog in all_blogs:
        if blog["id"] == blog_id:
            posted_blog = blog

    return render_template("post.html", blog=posted_blog)

if __name__ == "__main__":
    app.run(debug=True)
