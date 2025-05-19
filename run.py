import os
import subprocess
from IPython.display import Image, display
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Install necessary dependencies
subprocess.run(["pip", "install", "ultralytics==8.0.196", "--quiet"], check=True)

# Import ultralytics and check installation
import ultralytics
ultralytics.checks()

# Define dataset and configuration paths
dataset_path = "/media/user/DormGuardNet/Dataset/data.yaml"
config_path = "/media/user/18800322148/Jahid_project_DormGuardNet/Dormguard.yaml"

# Run YOLOv5 training
subprocess.run([
    "python", "train.py",
    "--img", "640",
    "--batch", "300",
    "--epochs", "200",
    "--data", dataset_path,
    "--cfg", config_path
], check=True)

# Define path to the results from training
train_results_path = "/media/user/DormGuardNet/yolov5/runs/train/exp"  # Adjust path as necessary

# Print results message
print("Training Results:")
img_results = mpimg.imread(f"{train_results_path}/results.png")
img_confusion = mpimg.imread(f"{train_results_path}/confusion_matrix.png")
plt.figure(figsize=(10, 10))

# Display results.png
plt.subplot(1, 2, 1)
plt.imshow(img_results)
plt.title("Training Results")
plt.axis('off')

# Display confusion_matrix.png
plt.subplot(1, 2, 2)
plt.imshow(img_confusion)
plt.title("Confusion Matrix")
plt.axis('off')

plt.show()

# Check if the validation prediction image exists
val_image_path = f"{train_results_path}/val_batch0_pred.jpg"

if os.path.exists(val_image_path):
    print("Validation Predictions:")
    img_val = mpimg.imread(val_image_path)
    plt.figure(figsize=(10, 10))
    plt.imshow(img_val)
    plt.title("Validation Predictions")
    plt.axis('off')
    plt.show()
else:
    print(f"Validation image not found at {val_image_path}. Please check the validation step.")
