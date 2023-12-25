import pandas as pd

def load_dataset(dataset_path):
    # Load the dataset from the CSV file
    dataset = pd.read_csv(dataset_path)
    return dataset

def save_dataset(dataset, output_path):
    # Save the dataset to a CSV file
    dataset.to_csv(output_path, index=False)