from flask import Flask
from flas_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config("SQLALCHEMY_DATABASE_URI")= "sqlite:///db.sqlite3.db"
app.config("SQLALCHEMY_TRAC_MODIFICATIONS")= False

db=SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)