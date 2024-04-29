from flask import Flask, request, Response
import requests

app = Flask(__name__)

API_KEYS = ['aa-aa-00-aa', 'aa-00-aa-aa']

@app.route('/proxy', methods=['POST'])
def proxy():
    api_key = request.headers.get('X-API-KEY')
    if api_key not in API_KEYS:
        return {'error': 'Недействительный API ключ'}, 403

    url = f"http://localhost:8899{request.full_path}"
    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers.items() if key != 'Host'},
        data=request.data,
    )

    return Response(
        response=response.content,
        status=response.status_code,
        headers=dict(response.headers),
    )

@app.route('/twit', methods=['POST'])
def proxy():
    api_key = request.headers.get('X-API-KEY')
    if api_key not in API_KEYS:
        return {'error': 'Недействительный API ключ'}, 403
    
    url = request.json.get('urlTwit')
    response = requests.request(
        method="get",
        url=url
    )

    return Response(
        response=response.content,
        status=response.status_code,
        headers=dict(response.headers),
    )

if __name__ == '__main__':
    app.run(host='144.202.63.224', port=3013)
