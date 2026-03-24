from flask import Flask, render_template, request, jsonify
from ai.recommender import generate_itinerary
from ai.safety import get_safety_info

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plan")
def plan():
    destination = request.args.get("dest")
    budget = request.args.get("budget")
    days = request.args.get("days")
    preference = request.args.get("pref")

    itinerary = generate_itinerary(destination, budget, days, preference)
    safety = get_safety_info(destination)

    return render_template(
        "result.html",
        destination=destination,
        itinerary=itinerary,
        safety=safety
    )

@app.route("/safety-details/<place>")
def safety_details(place):
    return jsonify(get_safety_info(place))

if __name__ == "__main__":
    app.run(debug=True)
