from parsers import parse_json_log, parse_csv_log, validate_log
from log_analysis.models import LogEvent
from datetime import datetime
def parsing_logs(log_data):
    parsed_data = parse_json_log(log_data)

    if parsed_data is not None:
        Log = LogEvent(
            timestamp=parsed_data.get("timestamp"),
            level=parsed_data.get("level"),
            message=parsed_data.get("message"),
            user_id=parsed_data.get("user", {}).get("id"),
            user_name=parsed_data.get("user", {}).get("name"),
            user_email=parsed_data.get("user", {}).get("email"),
            tags=",".join(parsed_data.get("tags", []))
        )
        Log.save()

        return True





def normalize_csv_log(parsed_data):
    normalized_data = []

    for log_entry in parsed_data:
        # Validate the log entry
        if not validate_log(log_entry):
            continue  # Skip invalid log entries

        # Apply normalization steps to each log entry
        log_entry['timestamp'] = datetime.strptime(log_entry['timestamp'], '%Y-%m-%d %H:%M:%S')
        log_entry['level'] = log_entry['level'].lower()

        # Save the log entry to the database using the Django model
        log = LogEvent(
            timestamp=log_entry['timestamp'],
            level=log_entry['level'],
            message=log_entry['message']
        )
        log.save()

        normalized_data.append(LogEvent)

    return normalized_data