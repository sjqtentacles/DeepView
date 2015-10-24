from flask import Flask, request,url_for, render_template, jsonify
import requests
import re
import time
import pickle

cpmodel = pickle.load(open("cp-score-old-model.pkl","rb"))

app = Flask(__name__)


@app.route('/stats')
@app.route('/stats/<input>')
def stats(input=None):
	whiteElo = request.args.get('whiteElo')
	blackElo = request.args.get('blackElo')
	engineScore = request.args.get('engineScore')
		
	if whiteElo and blackElo:
		return render_template("elodiff/stats.html")
	elif engineScore:
		if str(engineScore)[0]=='m':
			engineScore = int(str(engineScore[1:]))*-1
		whiteProb = round(cpmodel.predict(engineScore)[0],2)
		blackProb = round(1-whiteProb,2)*100
		whiteProb = whiteProb*100
		return render_template("elodiff/stats.html", cpWhiteProb = int(whiteProb), cpBlackProb = 100-int(whiteProb))	
	else:
		return render_template("elodiff/stats.html")
	
@app.route('/')
def root():
	return app.send_static_file('index/index.html')

	
if __name__ == "__main__":
	app.run(debug=True)
