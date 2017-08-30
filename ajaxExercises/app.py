from flask import Flask, url_for, render_template, jsonify
from flask_bootstrap import Bootstrap
from random import randint 



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
	number = randint(1,100)
	return render_template('index.html', number=number)

@app.route('/rando', methods=['POST'])
def rando(): 
	number = randint(1,100)
	return jsonify({"no":randint(1,100)})

if __name__=='__main__':
	app.run(debug=True)

