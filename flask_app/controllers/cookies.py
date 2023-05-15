from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import cookie



@app.route('/')
def index():
    all_orders = cookie.Cookie.get_all_orders()
    return render_template("orders_dashboard.html", all_orders = all_orders)

@app.route('/new/order')
def new_order():
    return render_template("new_order.html")

@app.route('/process/order', methods = ["POST"])
def process_order():
    if not cookie.Cookie.validate_cookie(request.form):
        return redirect(request.referrer)
    cookie.Cookie.add_order(request.form)
    return redirect('/')

@app.route('/edit/order/<int:id>')
def edit_cookie_order(id):
    data = {
        "id":id
    }
    one_order = cookie.Cookie.get_one_order(data)
    return render_template("edit_order.html", one_order = one_order)

@app.route('/process/update', methods = ["POST"])
def process_update():
    if not cookie.Cookie.validate_cookie(request.form):
        return redirect(request.referrer)
    cookie.Cookie.update_order(request.form)
    return redirect('/')



