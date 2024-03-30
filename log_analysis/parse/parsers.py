import json
import csv
import logging
import yaml
import re


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
        logging.error(error_message)
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


def parse_log_entry(log_entry, log_source_type):
    # Load the log parsing rules from the config.yaml file
    with open('config.yaml') as f:
        config = yaml.safe_load(f)

    # Find the corresponding log parsing rule based on the log source type
    for rule in config:
        if rule['log_source_type'] == log_source_type:
            required_fields = rule['required_fields']
            parsing_patterns = rule['parsing_patterns']
            break
    else:
        # Handle the case when no log parsing rule is found for the given log source type
        raise ValueError(f"No log parsing rule found for log source type: {log_source_type}")

    # Initialize an empty dictionary to store the parsed fields
    parsed_fields = {}

    # Iterate over the required fields and parsing patterns
    for field, pattern in zip(required_fields, parsing_patterns):
        # Use regular expressions to extract the field value from the log entry
        match = re.search(pattern, log_entry)
        if match:
            # Store the extracted field value in the parsed_fields dictionary
            parsed_fields[field] = match.group(1)
        else:
            # Handle the case when a required field cannot be extracted from the log entry
            raise ValueError(f"Failed to extract field '{field}' from log entry")

    # Return the parsed fields dictionary
    return parsed_fields
