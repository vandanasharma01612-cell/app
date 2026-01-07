from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from education import EducationAI
from user import register_user, login_user

app = Flask(__name__)
app.secret_key = "edugpt_secret"

ai = EducationAI()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if login_user(username, password):
            session["user"] = username
            return redirect(url_for("chat"))
        else:
            return "Invalid login"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if register_user(username, password):
            return redirect(url_for("login"))
        else:
            return "User already exists"

    return render_template("register.html")

@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
def api_chat():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"})

    question = request.json.get("question", "")
    answer = ai.generate_answer(question)
    return jsonify({"answer": answer})

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)