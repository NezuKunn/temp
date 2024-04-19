from django.http import JsonResponse, HttpResponse
import requests

# Здесь хранятся ваши API ключи
API_KEYS = ['aa-00-aa-aa', 'admin-key-temp']

def proxy(request):
    api_key = request.META.get('HTTP_X_API_KEY')
    if api_key not in API_KEYS:
        return JsonResponse({'error': 'Недействительный API ключ'}, status=403)

    url = f"http://localhost:8899{request.get_full_path()}"  # замените на URL вашего Solana RPC узла
    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for (key, value) in request.headers.items() if key != 'Host'},
        data=request.body,
    )

    return HttpResponse(
        content=response.content,
        status=response.status_code,
        content_type=response.headers['Content-Type']
    )