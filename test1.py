#!/bin/python3
import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)

# test = [
# 	{
# 	'test':'yes',
# 	'erorr':'no'
# 	}
# ]

@app.route('/status', methods=['GET'])
def get():
	out = subprocess.run(f'ping {request.args.get("ip")} -c 1 | python3 test2.py',
							shell=True, capture_output=True, text=True).stdout.split('\n')

	status = [
		{
			'ip': out[0],
			'time': out[1]
		}
	]
	return jsonify(status)

if __name__ == '__main__':
	#app.run(host='10.10.10.5',port=12000, debug=False)
	app.run()
