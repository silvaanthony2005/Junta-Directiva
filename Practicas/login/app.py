from flask import Flask

app = Flask(__name__)

@app.route("/login")
def login():
    return "/login"

@app.route("/logout")
def logout():
    return "/logout"

@app.route("/register")
def register():
    return "/register"

@app.route("/Dashboard")
def dashboard():
    return("/dashboard")

# lanzar app en modo debugging
if __name__ == "__main__":
    app.run(debug=True)