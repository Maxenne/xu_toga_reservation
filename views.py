from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def reserve_toga(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'status': 'Reservation received', 'data': data})
    return JsonResponse({'error': 'Invalid request'}, status=400)
