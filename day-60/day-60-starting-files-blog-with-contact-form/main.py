from flask import Flask, render_template, request
import requests
import smtplib

my_email = "YOUR EMAIL"
my_password = "YOUR PASSWORD"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",  methods=['POST', 'GET'])
def contact():
    sent_msg = False

    if request.method == 'POST':
        sent_msg = True
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP(host="173.194.193.108", port=587,) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="YOUR EMAIL",
                                msg=f"{name}\n{email}\n{phone}\n{message}")
        return render_template("contact.html", sent_msg=sent_msg)
    else:
        return render_template("contact.html", sent_msg=sent_msg)



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)





if __name__ == "__main__":
    app.run(debug=True, port=5001)
