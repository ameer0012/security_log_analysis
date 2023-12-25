from django.shortcuts import render
from .models import LogEvent
from .parse.parsing import parsing_logs, normalize_csv_log
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from logs_receiver import receive_log
from .parse.parsers import parse_json_log,parse_csv_log


@csrf_exempt  # Disable CSRF protection for this view

def receive_logs(request):
    if request.method == 'POST':
        log_data = request.body.decode('utf-8')
        content_type = request.content_type
        log_file = receive_log(log_data, content_type, logs_directory='home/logs')
        if content_type == 'application/json':
            # Parse the log data using the JSON log parser
            parsed_log_dat = parse_json_log(log_file)
            parsing_logs(parsed_log_dat)
        elif content_type == 'text/csv':
            parsed_log_dat = parse_csv_log(log_file)
            normalize_csv_log(parsed_log_dat)
        else:
            return HttpResponse(status=400)

        if parsed_log_dat is None:
            return HttpResponse(status=400)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

def log_list(request):
    logs = LogEvent.objects.all()
    return render(request, 'log_analysis/log_list.html', {'logs': logs})