from dataset_utils import load_dataset, save_dataset
from preparation import preprocess_dataset

# Path to the dataset CSV file
dataset_path = 'datasets/labelled_validation_data.csv'

# Path to save the preprocessed dataset
preprocessed_dataset_path = 'datasets/preprocess/labelled_preprocess_validation_data.csv'

# Load the dataset
dataset = load_dataset(dataset_path)

# Preprocess the dataset
preprocessed_dataset = preprocess_dataset(dataset)

# Save the preprocessed dataset
save_dataset(preprocessed_dataset, preprocessed_dataset_path)

print("Preprocessing complete. Preprocessed dataset saved to", preprocessed_dataset_path)