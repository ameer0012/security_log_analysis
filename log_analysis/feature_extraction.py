def extract_features(log):
    # Implement your feature extraction logic here
    # This function should extract relevant features from the log entry

    # Replace the following sample code with your own feature extraction logic
    features = {
        'source': log.source,
        'message_length': len(log.message),
        # Add more features as needed
    }

    return features