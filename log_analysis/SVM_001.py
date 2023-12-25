import keras.layers
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from keras.models import Model
from keras.layers import Input, Dense
from keras import backend as ke
from keras.losses import mse
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load the preprocessed dataset
preprocessed_dataset_path = 'datasets/preprocess/labelled_preprocess_training_data.csv'
dataset = pd.read_csv(preprocessed_dataset_path)

# Load the test dataset
test_dataset_path = 'datasets/preprocess/labelled_preprocess_testing_data.csv'
test_dataset = pd.read_csv(test_dataset_path)

# Load the validation dataset
validation_dataset_path = 'datasets/preprocess/labelled_preprocess_validation_data.csv'
validation_dataset = pd.read_csv(validation_dataset_path)

# Identify columns with string values
columns_with_strings = ['processName', 'hostName', 'args']  # Replace with actual column names

# Encode categorical variables
label_encoder = LabelEncoder()
for column in columns_with_strings:
    if column in dataset.columns:
        dataset[column] = label_encoder.fit_transform(dataset[column])
    if column in test_dataset.columns:
        test_dataset[column] = label_encoder.fit_transform(test_dataset[column])
    if column in validation_dataset.columns:
        validation_dataset[column] = label_encoder.fit_transform(validation_dataset[column])

# Convert non-categorical string values to numeric
#non_categorical_columns = ['args']
#for column in non_categorical_columns:
 #   if column in dataset.columns:
  #      dataset[column] = dataset[column].astype(float)
   #     test_dataset[column] = test_dataset[column].astype(float)
    #    validation_dataset[column] = validation_dataset[column].astype(float)


# Split the preprocessed dataset into features (X) and labels (y)
X = dataset.drop(['sus', 'evil'], axis=1)
y = dataset[['sus', 'evil']]

# Split the test dataset into features (X_test) and labels (y_test)
X_test = test_dataset.drop(['sus', 'evil'], axis=1)
y_test = test_dataset[['sus', 'evil']]

# Split the validation dataset into features (X_val) and labels (y_val)
X_val = validation_dataset.drop(['sus', 'evil'], axis=1)
y_val = validation_dataset[['sus', 'evil']]

# Create an instance of MultiLabelBinarizer
label_binarizer = MultiLabelBinarizer()

# Combine 'sus' and 'evil' labels into a single column
y_combined = [(row['sus'], row['evil']) for _, row in y.iterrows()]

# Fit and transform the combined labels using MultiLabelBinarizer
y_binarized = label_binarizer.fit_transform(y_combined)

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)
X_val_scaled = scaler.transform(X_val)

# VAE Model
input_dim = X_scaled.shape[1]
latent_dim = 2  # Adjust the latent dimension based on your needs

# Encoder
input_layer = Input(shape=(input_dim,))
encoder_hidden = Dense(64, activation='relu')(input_layer)
z_mean = Dense(latent_dim)(encoder_hidden)
z_log_var = Dense(latent_dim)(encoder_hidden)

# Sampling
def sampling(args):
    z_mean, z_log_var = args
    epsilon = ke.random_normal(shape=(ke.shape(z_mean)[0], latent_dim), mean=0., stddev=1.)
    return z_mean + ke.exp(z_log_var / 2) * epsilon

z = keras.layers.Lambda(sampling)([z_mean, z_log_var])

# Decoder
decoder_hidden = Dense(64, activation='relu')(z)
output_layer = Dense(input_dim)(decoder_hidden)

# VAE Model
vae = Model(input_layer, output_layer)

# VAE Loss
reconstruction_loss = mse(input_layer, output_layer)
kl_loss = -0.5 * ke.mean(1 + z_log_var - ke.square(z_mean) - ke.exp(z_log_var), axis=-1)
vae_loss = ke.mean(reconstruction_loss + kl_loss)

vae.add_loss(vae_loss)
vae.compile(optimizer=Adam())

# Now, let's train the VAE model using the preprocessed dataset.


# Train the VAE model
vae.fit(X_scaled, epochs=10, batch_size=32, validation_data=(X_val_scaled, None))

# Obtain the latent space representation
encoder = Model(input_layer, z_mean)

# Encode the preprocessed dataset
X_encoded = encoder.predict(X_scaled)

# DOSE Model
svm_classifier = SVC()
svm_classifier.fit(X_encoded, y_binarized)

# Encode the test dataset using the trained encoder
X_test_encoded = encoder.predict(X_test_scaled)

# Predict the labels for the test set
y_pred_test = svm_classifier.predict(X_test_encoded)

# Calculate the accuracy of the model on the test set
accuracy_test = accuracy_score(y_test, y_pred_test)
print("Accuracy on test set:", accuracy_test)