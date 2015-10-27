from flask import Flask, request,url_for, render_template, jsonify
import requests
import re
import time
import pickle

cpmodel = pickle.load(open('cp-score-old-model.pkl','rb'))

app = Flask(__name__)


@app.route('/stats')
@app.route('/stats/<input>')
def stats(input=None):
	engineScore = request.args.get('engineScore')
	if engineScore:
		if str(engineScore)[0]=='m':
			engineScore = int(str(engineScore[1:]))*-1
		whiteProb = round(cpmodel.predict(engineScore)[0],2)
		blackProb = round(1-whiteProb,2)*100
		whiteProb = whiteProb*100
		return render_template('stats.html', cpWhiteProb = int(whiteProb), cpBlackProb = 100-int(whiteProb))	
	else:
		return render_template('stats.html')
		
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/')
def root():
	return render_template('index.html')

	
if __name__ == "__main__":
	app.run(debug=True)
