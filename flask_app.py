from flask import Flask
import os
import models
import controllers

app = Flask(__name__)
models.init_db()
app.secret_key = os.urandom(24)


app.register_blueprint(controllers.bp)

if __name__ == "__main__":
    models.init_db()
    app.run(debug=True)