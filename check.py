from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_DIR = "TrashIQ_Dataset"

datagen = ImageDataGenerator(rescale=1./255)

data = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(224,224),
    batch_size=32,
    class_mode="categorical"
)

print("\n✅ CLASS INDEX MAPPING:")
print(data.class_indices)
