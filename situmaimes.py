from flask import Flask,render_template,request,redirect,url_for,flash
import json
import codecs
import sqlite3
app=Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
@app.route("/score")
def score():
    return render_template("score.html")

@app.route("/submit",methods=["POST"])
def submit():
    conn = sqlite3.connect("score.db")
    c=conn.cursor()
    print(request.form["bioChem"], request.form["id"], request.form["cet4"])
    if (int(request.form["id"]),request.form["name"]) in sanbanlist:
        if request.form["bioChem"] and request.form["cet4"]:
            c.execute("UPDATE midterm set bioChem = {bioChem},cet4={cet4} where id={id}".format(bioChem=request.form["bioChem"], id=request.form["id"],
                                                                                cet4=request.form["cet4"]))
            conn.commit()
        for i in c.execute("select * from midterm"):
            print(i)
        conn.close()
        return render_template("base.html")
    else:
        flash("不要乱输 谢谢")
        return redirect(url_for('score'))

def prepare():
    global sanbanlist
    with codecs.open(r"C:\Personal Files\projects\files\三班.json", encoding="utf-8") as f:
        sanban = json.loads(f.read())
    sanbanlist = [(sanban[i]["学号"], i) for i in sanban]
    conn = sqlite3.connect("score.db")
    c = conn.cursor()
    tables = c.execute("select name from sqlite_master where type == 'table' ").fetchone()
    if (not tables) or "midterm" not in tables:
        creatsSql = """
            create table midterm
            (id int PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            bioStatic real,
            bioChem real,
            physics real,
            diangong real,
            wuhua real,
            cet4 text);"""
        c.execute(creatsSql)
        c.executemany("insert into midterm (id,name) values(?,?)", sanbanlist)
        for i in c.execute("select * from midterm"):
            print(i)
    conn.commit()
    conn.close()

if __name__=="__main__":
    prepare()
    app.run("0.0.0.0",debug=True)