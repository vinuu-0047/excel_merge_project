import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and store it in a DataFrame named user_list
user_list = pd.read_csv("user_list.csv")

# Print a heading for dataset overview
print("\n----- DATASET OVERVIEW -----")

# Display number of rows and columns in the dataset
print("Shape of Dataset:", user_list.shape)

# Print a heading for column names
print("\nColumn Names:")

# Convert column names into a Python list and display them
print(user_list.columns.tolist())

# Print a heading for missing values analysis
print("\nMissing Values:")

# Count missing (null) values in each column and display them
print(user_list.isnull().sum())

# Print a heading for data type information
print("\nData Types:")

# Display data type of every column
print(user_list.dtypes)


# Data Cleaning Section
# Loop through Gender, Category, and Group columns
for col in ["Gender", "Category", "Group"]:
    
    # Convert values to string format
    # Remove extra spaces from beginning/end
    # Capitalize first letter of each word
    user_list[col] = user_list[col].astype(str).str.strip().str.title()

# 1. Gender Distribution Chart

# Create a figure with width=6 inches and height=4 inches
plt.figure(figsize=(6,4))

# Count occurrences of each gender and create a bar chart
ax1 = user_list["Gender"].value_counts().plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

# Set chart title
plt.title("Gender Distribution")

# Label X-axis
plt.xlabel("Gender")

# Label Y-axis
plt.ylabel("Count")

# Display exact count values on top of bars
ax1.bar_label(ax1.containers[0])

# Adjust spacing so labels are not cut off
plt.tight_layout()

# Display the chart
plt.show()

# 2. Category Distribution Chart

# Create a new figure
plt.figure(figsize=(6,4))

# Count occurrences of each category and create a bar chart
ax2 = user_list["Category"].value_counts().plot(
    kind="bar",
    color="lightgreen",
    edgecolor="black"
)

# Set chart title
plt.title("Category Distribution")

# Label X-axis
plt.xlabel("Category")

# Label Y-axis
plt.ylabel("Count")

# Show count values above bars
ax2.bar_label(ax2.containers[0])

# Prevent labels from being cut off
plt.tight_layout()

# Display chart
plt.show()

# 3. Group Distribution Chart

# Create a new figure
plt.figure(figsize=(6,4))

# Count occurrences of each group and create a bar chart
ax3 = user_list["Group"].value_counts().plot(
    kind="bar",
    color="salmon",
    edgecolor="black"
)

# Set chart title
plt.title("Group Distribution")

# Label X-axis
plt.xlabel("Group")

# Label Y-axis
plt.ylabel("Count")

# Display exact count values on bars
ax3.bar_label(ax3.containers[0])

# Adjust spacing
plt.tight_layout()

# Display chart
plt.show()