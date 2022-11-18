from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
import numbers


@csrf_exempt
def calculate_view(request: WSGIRequest):
    if not request.method == 'POST':
        return HttpResponseNotAllowed('Only POST request are allowed')

    if not request.body:
        response = JsonResponse({'error': 'No data'})
        response.status_code = 400
        return response

    nums = json.loads(request.body)
    a = nums.get('A')
    b = nums.get('B')

    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        response = JsonResponse({'error': 'No numbers'})
        response.status_code = 400
        return response

    if request.path == '/add/':
        answer = {'answer': a + b}
    if request.path == '/subtract/':
        answer = {'answer': a - b}
    if request.path == '/multiply/':
        answer = {'answer': a * b}
    if request.path == '/divide/':
        if b == 0:
            response = JsonResponse({'error': 'Division by zero!'})
            response.status_code = 400
            return response
        answer = {'answer': a / b}
    return JsonResponse(answer)


def index_view(request):
    return render(request=request, template_name='index.html')
