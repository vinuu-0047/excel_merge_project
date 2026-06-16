# Read the dataset from CSV file
data <- read.csv("C:/Users/HP/Downloads/excel_merge_project(final)/user_list.csv")

# Display first few records
head(data)

# Display structure of dataset
str(data)

# Select Total Learning Hours column
hours <- data$Total_Learning_Hours

# Calculate mean
mean_value <- mean(hours)

# Calculate median
median_value <- median(hours)

# Calculate mode
mode_value <- as.numeric(names(sort(table(hours), decreasing = TRUE)[1]))

# Calculate range
range_value <- max(hours) - min(hours)

# Calculate variance
variance_value <- var(hours)

# Calculate standard deviation
sd_value <- sd(hours)

# Print mean value
cat("Mean =", mean_value, "\n")

# Print median value
cat("Median =", median_value, "\n")

# Print mode value
cat("Mode =", mode_value, "\n")

# Print range value
cat("Range =", range_value, "\n")

# Print variance value
cat("Variance =", variance_value, "\n")

# Print standard deviation value
cat("Standard Deviation =", sd_value, "\n")