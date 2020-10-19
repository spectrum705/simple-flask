from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "key-sama"

memo = [ {
        "author": "Spectrum",
        "title": "DarkKnight",
        "content": "I speak in a deep voice. I'm batman.",
        "date": "29 Jan"    
        },
        
        {
        "author": "Mooshoo",
        "title": "Weirdo",
        "content": "I am a weirdo, there's nothing to it.",
        "date": "7 Mar"    
        },
    
    
    
    
    
]


@app.route('/')
def home():
    
    return render_template("index.html")


@app.route('/view')
def view():
    return render_template("view.html", posts= memo)


@app.route('/about')
def about():
    return render_template("about.html")




@app.route('/add', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        
        person = request.form["nm"]
        session["user"] = person
        return "added!"
    
    
    
    else:
        return render_template('add.html')
    
    



if __name__  == "__main__":
    
    app.run(debug = True)