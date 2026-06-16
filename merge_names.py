import pandas as pd
# pandas library is imported to handle data manipulation and analysis tasks.
user_list = pd.read_csv("user_list.csv")
employee_master = pd.read_excel("employee master list.xlsx")
#read user_list and Employee_Master 
user_list["Full_Name"] = (user_list["Full_Name"]  #data cleaning 
    .astype(str) #convert to string
    .str.strip() #remove whitespaces
    .str.upper() #convert to uppercase
)
user_list = user_list.drop_duplicates(subset=["Full_Name"])  #remove duplicates based on Full_Name
employee_master["NAME"] = (employee_master["NAME"]   #data cleaning
    .astype(str) #convert to string
    .str.strip() #remove whitespaces
    .str.upper() #convert to uppercase
)

result = employee_master.merge( #merging the data 
    user_list[
        [
            "Full_Name","Gender","Category","Phone_Number","Group"          
        ]
    ],
    left_on="NAME",
    right_on="Full_Name",
    how="left"
)
result.drop(columns=["Full_Name"], inplace=True)
unmatched = result[result["Gender"].isna()]

print("\nSample unmatched names:")
print(unmatched["NAME"].head(20).tolist())
result.to_excel("employee_master_updated.xlsx", index=False) #save the merged data to a new Excel file
print("Output file: employee_master_updated.xlsx")
print("Rows in master file:", len(employee_master))
print("Rows in output file:", len(result))

print("Missing Phone Numbers:", result["Phone_Number"].isna().sum())
print("Missing Groups:", result["Group"].isna().sum())

print("Matched records:", result["Gender"].notna().sum())
print(user_list[["Full_Name", "Employee_Id"]].head(20))
print(employee_master[["NAME", "PERNO"]].head(20))
