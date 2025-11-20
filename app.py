from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():

    name = "นายเอกณัฐ เกียรตินันทน์"
    student_id = "672347"

    github_url = "https://github.com/67112347-Pun/ce341-flask-web.git"
    dockerhub_url = "https://hub.docker.com/repositories/punqazwsx1122"

    return render_template(
        "home.html",
        name=name,
        student_id=student_id,
        github_url=github_url,
        dockerhub_url=dockerhub_url
    )
@app.route("/git")
def git_page():
    return render_template("git.html")
@app.route("/docker")
def docker_page():