from flask import Flask, render_template, request
from education import EducationAgent

app = Flask(__name__)
agent = EducationAgent()

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = agent.generate_answer(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)