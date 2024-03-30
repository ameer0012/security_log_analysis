import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def receive_syslog(request):
    logger.debug('Received Syslog log: %s', request.body)

    return HttpResponse(status=200)
