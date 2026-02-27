from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # We'll make the home page the instructions
    return render_template('instructions.html')

@app.route('/mission')
def mission():
    # This route will launch the actual game
    return render_template('gravity.html')

if __name__ == '__main__':
    app.run(debug=True)