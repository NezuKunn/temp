from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup

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
def twit():
    api_key = request.headers.get('X-API-KEY')
    if api_key not in API_KEYS:
        return {'error': 'Недействительный API ключ'}, 403
    
    url = request.json.get('urlTwit')
    response = requests.request(
        method="get",
        url=url
    )

    results = []

    soup = BeautifulSoup(response.text, 'lxml')
    mainblock = soup.find('div', class_='css-175oi2r r-1kbdv8c r-18u37iz r-1oszu61 r-3qxfft r-s1qlax r-2sztyj r-1efd50x r-5kkj8d r-h3s6tt r-1wtj0ep r-1igl3o0 r-rull8r r-qklmqi')
    blocks = mainblock.find_all('div', class_='css-175oi2r r-18u37iz r-1h0z5md r-13awgt0')

    for block in blocks:
        span = block.find('span', class_='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3')
        text = span.text
        results.append(text)

    return Response(
        response=results,
        status=response.status_code,
        headers=dict(response.headers),
    )

if __name__ == '__main__':
    app.run(host='144.202.63.224', port=3013)
