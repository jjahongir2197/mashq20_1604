from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def year_check():

    if request.method == "POST":

        year = int(request.form["year"])

        if year > 2000:
            return "Yil 2000 dan katta"
        else:
            return "Yil 2000 dan kichik yoki teng"

    return render_template("index.html")

app.run(debug=True)
