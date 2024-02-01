import json
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Controller


@csrf_protect
@csrf_exempt
def handle_controller_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            controller_data = data.get('messages')[0]
            controller = Controller.objects.create(
                type=data.get('type'),
                sn=data.get('sn'),
                fw=controller_data.get('fw'),
                conn_fw=controller_data.get('conn_fw'),
                active=controller_data.get('active'),
                mode=controller_data.get('mode'),
                controller_ip=controller_data.get('controller_ip')
            )

            # Дополнительная логика, если необходимо

            response_data = {
                'status': 'success',
                'message': 'Controller data received and saved.'
            }
            return JsonResponse(response_data)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Invalid JSON format: {e}'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)