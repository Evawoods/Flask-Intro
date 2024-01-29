from flask import Flask, request
from operations import add, sub, mult, div

# Part 1
app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract b from a"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route("/div")
def do_div():
    """divide a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

# Part 2
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operator>")
def do_math(operator):
    """Do math operator of a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a,b)

    return str(result)