from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():

    return render_template("home.html")



@app.route('/shop')
def shop_page():
	fruitlist = ['apple' , 'banana', 'mango','pineapple', 'pear', 'orange', 'melon']
	return render_template("shop.html", fruits = fruitlist)



if __name__ == '__main__':
   app.run(debug = True)