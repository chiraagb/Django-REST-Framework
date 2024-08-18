from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hey there!! This is your Django API response."})
