import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def receive_syslog(request):
    logger.debug('Received Syslog log:', request.body)
    # Process and store the received log as needed
    return HttpResponse(status=200)
