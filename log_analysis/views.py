import yaml
from .models import LogEvent
from .parse.parsing import parsing_logs, normalize_csv_log
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import log_analysis.logs_receiver
from .parse.parsers import parse_json_log,parse_csv_log
import logging
from django.shortcuts import render, redirect
from .forms import LogParsingRuleForm , LogParsingRuleAddForm
from .models import LogParsingRule

@csrf_exempt  # Disable CSRF protection for this view

def receive_logs(request):
    if request.method == 'POST':
        log_data = request.body.decode('utf-8')
        content_type = request.META.get('CONTENT_TYPE', '')
        log_file = log_analysis.logs_receiver.receive_log(log_data, content_type, logs_directory='home/logs')
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
            return HttpResponse(status=403)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

def log_list(request):
    logs = LogEvent.objects.all()
    return render(request, 'log_analysis/log_list.html', {'logs': logs})

logger = logging.getLogger(__name__)

#def receive_syslog(request):
    #if request.method == 'POST':
       # log_message = request.POST.get('log_message')
       # logger.info(log_message)
       # return HttpResponse(status=200)
  #  else:
     #   return HttpResponse(status=405)


def receive_syslog(request):
    if request.method == 'POST':
        log_message = request.body.decode('utf-8')  # Assuming the log message is sent in the request body
        LogEvent.objects.create(message=log_message)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def index(request):
    rules = LogParsingRule.objects.all()
    return render(request, 'log_analysis/index.html', {'rules': rules})


def edit_config(request):
    global add_form
    if request.method == 'POST':
        if 'add_rule' in request.POST:
            form = LogParsingRuleAddForm(request.POST)
            if form.is_valid():
                log_source_type = form.cleaned_data['\n log_source_type']
                required_fields = form.cleaned_data['required_fields'].split('\n')
                parsing_patterns = form.cleaned_data['parsing_patterns'].split('\n')

                with open('log_analysis/config.yaml', 'a') as f:
                    yaml.dump([{
                        'log_source_type': log_source_type,
                        'required_fields': required_fields,
                        'parsing_patterns': parsing_patterns
                    }], f)

                return redirect('log_analysis:index')
        else:
            form = LogParsingRuleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('log_analysis:index')
    else:
        form = LogParsingRuleForm()
        add_form = LogParsingRuleAddForm()
    return render(request, 'log_analysis/config_form.html', {'form': form, 'add_form': add_form})