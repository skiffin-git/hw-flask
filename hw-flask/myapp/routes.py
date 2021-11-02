from myapp import myobj
from myapp.forms import TopCities
from myapp.models import City
from myapp import db
from flask import render_template, escape, flash, redirect

@myobj.route("/", methods = ["POST", "GET"])
def home():
    title = "Top Cities"
    name = "Vlad"
    form = TopCities()
    if form.validate_on_submit():
        city = City(city_name = form.city_name.data, city_rank = form.city_rank.data, is_visited = form.is_visited.data)
        db.session.add(city)
        db.session.commit()
        return redirect("/")
    cities = City.query.all()
    return render_template("home.html", title = title, name = name, form = form, top_cities = cities)
