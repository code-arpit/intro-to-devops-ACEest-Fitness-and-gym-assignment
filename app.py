from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

# In-memory store for workouts
workouts = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        workout = request.form.get("workout")
        duration = request.form.get("duration")
        if not workout or not duration:
            flash("Please enter both workout and duration.")
        else:
            try:
                duration = int(duration)
                workouts.append({"workout": workout, "duration": duration})
                flash(f"'{workout}' added successfully!")
            except ValueError:
                flash("Duration must be a number.")
    return render_template("index.html", workouts=workouts)


if __name__ == "__main__":
    app.run(debug=True)
