from preparation import preprocess_dataset

# Path to the dataset CSV file
dataset_path = "datasets/labelled_training_data.csv"

# Preprocess the dataset
preprocessed_dataset = preprocess_dataset(dataset_path)

# Print the preprocessed dataset
print(preprocessed_dataset.head())