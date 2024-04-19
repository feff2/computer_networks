from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/parse', methods=['GET'])
def parse_url():
    url = request.args.get('url')
    
    command = ['py', 'm_parser.py', '--url', url]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if error:
        return jsonify({'error': error.decode('utf-8')})
    else:
        return jsonify({'data': output.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)