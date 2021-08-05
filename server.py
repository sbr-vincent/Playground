from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def display_three_boxes():
    return render_template("index.html", num=3)	# notice the 2 new named arguments!

@app.route('/play/<int:num>')
def display_many_boxes(num):
    return render_template("index.html", num= num)

@app.route('/play/<int:num>/<string:color>')
def change_color(num,color):
    return render_template("index.html", num= num, color=color)

if __name__=="__main__":
    app.run(debug=True)

