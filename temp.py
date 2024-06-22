from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/raydium_data', methods=['POST'])
def proxy():
    print(request.json())

    return Response(
        response={"d": "a"},
        status=200
    )
if __name__ == '__main__':
    app.run(host='185.231.155.69', port=8014)
