import pandas as pd

user_list = pd.read_csv("user_list.csv")
employee_master = pd.read_excel("employee master list.xlsx")

print("user list columns:", user_list.columns.tolist())
print("employee master columns:", employee_master.columns.tolist())
