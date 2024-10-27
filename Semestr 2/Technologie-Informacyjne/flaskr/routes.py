import bp as bp
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
import matplotlib.pyplot as plt
import os
import numpy as np

bp = Blueprint("plots", __name__)


# ============= ROUTES HANDLING ================================
@bp.route("/")
def index():
    return render_template("home.html")


@bp.route("/home")
def home():
    return render_template("home.html")


@bp.route("/authors")
def authors():
    return render_template("authors.html")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/examples")
def examples():
    return render_template("examples.html")


@bp.route("/theory")
def theory():
    return render_template("theory.html")


@bp.route("/plots", methods=("GET", "POST"))
def plots():
    if request.method == "POST":
        x = request.form["variable"]
        coeffs = list(map(lambda n:float(n), x.split(";")))
        gen_and_save_plot(coeffs)
    return render_template("plots.html")


# ============= UTILITY FUNCTIONS ================================
def calc_poly_from_coeffs(x, coeffs):
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y


def gen_and_save_plot(coeffs):
    x = np.linspace(-30, 30, 300)
    if os.path.exists("flaskr\\static\\plots_img\\plot.png"):
        os.remove("flaskr\\static\\plots_img\\plot.png")
    plt.plot(x, calc_poly_from_coeffs(x, coeffs))
    plt.savefig("flaskr\\static\\plots_img\\plot")
    plt.close()
