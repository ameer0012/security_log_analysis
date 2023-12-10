def prepare_data(logs):
    # Implement your data preparation logic here
    # This function should convert the log data into a structured dataset with labeled data
    # Each log entry should be represented by features that capture relevant information for the machine learning model

    # Replace the following sample code with your own data preparation logic
    prepared_data = []

    for log in logs:
        if 'error' in log.message.lower():
            prepared_data.append((log, 1))  # Labeling as a security incident
        else:
            prepared_data.append((log, 0))  # Labeling as a non-incident

    return prepared_data