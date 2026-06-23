from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_resume():

    file = request.files["resume"]

    if file:

        score = 85

        suggestions = [
            "Add more projects",
            "Include GitHub profile",
            "Add certifications",
            "Add internship experience"
        ]

        return render_template(
            "result.html",
            score=score,
            suggestions=suggestions
        )


if __name__ == "__main__":
    app.run(debug=True)
