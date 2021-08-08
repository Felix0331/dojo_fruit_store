from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    x = int(request.form['apple'])+int(request.form['raspberry'])+int(request.form['strawberry'])
    print(f"Charging {request.form['first_name']} for {x} fruits ")
    return render_template("checkout.html", user_info = request.form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    