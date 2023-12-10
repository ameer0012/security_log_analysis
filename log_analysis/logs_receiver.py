import os
import datetime
import uuid

def receive_log(log_data, content_type, logs_directory):
    # Create the logs directory if it doesn't exist
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    # Generate a unique filename based on the current timestamp and a UUID
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4().hex)
    filename = f"log_{timestamp}_{unique_id}"

    # Determine the file extension based on the content type
    if content_type == "application/json":
        filename += ".json"
    elif content_type == "text/csv":
        filename += ".csv"
    else:
        # Handle unsupported content types or log formats
        return

    # Write the log data to the appropriate file
    log_file_path = os.path.join(logs_directory, filename)
    with open(log_file_path, "w") as log_file:
        log_file.write(log_data)

    # Optional: Return the path of the saved log file for further processing
    return log_file_path