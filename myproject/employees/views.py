from django.shortcuts import render
from .models import Event
from rest_framework import generics
from .serializers import EventSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Controller

@csrf_exempt
def handle_power_on(request):
    if request.method == 'POST':
        data = request.POST.get('data', None)

        if data and data == 'POWER_ON':
            # Проверяем, существует ли контроллер
            controller, created = Controller.objects.get_or_create(
                power_on=True, 
                offline=True, 
                operation_mode='normal'
            )

            # Если контроллер только что создан, добавьте логику для установки active
            if created:
                # Ваш код для установки контроллера в режим active, например:
                controller.set_active = True
                controller.save()

            # Отправляем ответ
            response_data = {
                'message': 'Контроллер offline, режим работы normal',
            }
            return JsonResponse(response_data)

    return JsonResponse({'error': 'Неверный запрос'}, status=400)