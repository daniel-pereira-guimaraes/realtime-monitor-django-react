import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@csrf_exempt
def send_message(request):
    
    if request.method == 'POST':
    
        data = json.loads(request.body)
        message = data.get('message', '')

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'monitor',
            {
                'type': 'broadcast_message',
                'message': message
            }
        )

        return JsonResponse({'status': 'ok'})