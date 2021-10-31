from flask import Flask,render_template, request, flash

app = Flask(__name__)
app.secret_key = 'password'

@app.route("/")
def index():
    flash("Enter a sphere radius:")
    return render_template("index.html")

@app.route("/sphere_volume", methods=["POST", "GET"])
def sphere_volume():
    def sphere_volume(r):
        pi = 3.141592653589793
        volume = 4/3*pi*r**3
        return(volume)

    r = request.form['radius_input']
    try:
        r = float(r)
        if r <= 0:
            flash('The radius is invalid.')
            flash('Please enter a valid radius:')
        else:
            flash('The volume of the sphere is ' + str(sphere_volume(r)))
            flash('Enter another sphere radius:')
    except ValueError:
        flash('The radius is invalid.')
        flash('Please enter a valid radius:')
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)