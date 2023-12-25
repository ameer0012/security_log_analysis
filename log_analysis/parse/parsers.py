import json
import csv
def parse_json_log(log_file):
    try:
        parsed_data = json.loads(log_file)
        if validate_log(parsed_data):
            return parsed_data
        else:
            return None
    except json.JSONDecodeError as e:
        # Log the error or raise an exception with a detailed message
        error_message = f"Error decoding JSON log: {e}"
        # Log the error message or raise an exception
        # logger.error(error_message)
        return None
def validate_log(parsed_data):
    required_fields = ["timestamp", "level", "message"]
    if all(field in parsed_data for field in required_fields):
        if not isinstance(parsed_data["timestamp"], str):
            return False
        if parsed_data["level"] not in ["INFO", "WARNING", "ERROR"]:
            return False
        if not parsed_data["message"]:
            return False
        return True
    else:
        return False



def parse_csv_log(log_file):
    parsed_data = []
    reader = csv.reader(log_file.splitlines())
    headers = next(reader)  # Assume the first row contains the column headers

    for row in reader:
        log_entry = {}
        for i, value in enumerate(row):
            # Handle empty values or missing columns
            if i < len(headers):
                log_entry[headers[i]] = value
            else:
                log_entry[f"column_{i+1}"] = value
        parsed_data.append(log_entry)

    return parsed_data
