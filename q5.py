import pandas as pd

filename = "data/student_performance.csv"
df = pd.read_csv(filename)

print("--- First 5 Rows ---")
print(df.head())
print("\n--- Dataset Shape (Rows, Columns) ---")
print(df.shape)
print("\n--- List of Column Names ---")
print(df.columns)
print("\n--- Check for Missing Values ---")
print(df.isnull().sum())
average_score = df["Final_Score"].mean()
print("\nAverage Final Score:", average_score)
highest_score = df["Final_Score"].max()
top_student = df[df["Final_Score"] == highest_score]
print("\nTop Student:")
print(top_student)
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
high_attendance_df = df[df["Attendance"] >= 80]
print("\nStudents with High Attendance (80% or more):")
print(high_attendance_df)
df_sorted = df.sort_values(by="Final_Score", ascending=False)
print("\nData Sorted by Final Score:")
print(df_sorted)
output_filename = "data/processed_student_performance.csv"
df_sorted.to_csv(output_filename, index=False)
print("\nSuccessfully saved the processed data to:", output_filename)