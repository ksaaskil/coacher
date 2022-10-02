from celery.result import AsyncResult
from django.db import connection
from django.http import JsonResponse

from coacher.reminders.tasks import debug_task
from coacher.celery import app

def debug(request):
    res = debug_task.delay()
    return JsonResponse({ "id": res.id, "url": f"/reminders/debug/{res.id}"})

def debug_by_id(request, debug_id: str):
    res = AsyncResult(debug_id, app=app)
    return JsonResponse({"id":res.id,"result":res.result})
