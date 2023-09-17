from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
app=  Flask(__name__)



# =====================>>><<<=====================
@app.route('/')
def main():
    return render_template("index.html")


@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>50:
        res="Passed"
    else:
        res="Failed"
    jak={"result":res, "score":score}
    
    return render_template("result.html", marks=jak)


@app.route("/submit", methods=["POST","GET"])
def submit():
    if request.method=="POST":
        science=float(request.form['science'])
        ds=float(request.form['ds'])
        math=float(request.form['math'])
        total=(science+math+ds)/3

    return redirect(url_for ('success', score=total) )
        


if __name__=="__main__":
    app.run(debug=True)
    # app.run()