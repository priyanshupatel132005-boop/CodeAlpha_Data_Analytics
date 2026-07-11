import pandas as pd

def advanced_large_data_pipeline_clean():
    print("====== Starting Data Preprocessing (No-Seaborn Version) ======")
    
    # Expanded dataset with 40 students and multiple courses for perfect Tableau dashboards
    raw_data = {
        'Student_ID': list(range(101, 141)),
        'Name': [
            '  Piyush ', 'Anjali', ' Rohan', 'Sneha  ', 'Amit', 'Pooja', 'Rahul', 'Kiran', 'Sanjay', 'Neha',
            'Vikram ', 'Deepak', 'Jyoti', 'Aman  ', 'Preeti', 'Nitin', 'Alok', 'Divya', 'Rajesh', 'Kavita',
            '  Manoj ', 'Swati', 'Harish', 'Ritu  ', 'Gaurav', 'Megha', 'Abhishek', 'Shalini', 'Pankaj', 'Komal',
            'Suresh ', 'Nisha', 'Vijay', 'Aarti  ', 'Sunil', 'Sapna', 'Varun', 'Monika', 'Arjun', 'Riya'
        ],
        'Course': [
            'BCA', 'BCA', 'B.Tech', 'BCA', 'B.Tech', 'BCA', 'B.Tech', 'BCA', 'B.Tech', 'B.Tech',
            'MCA', 'MCA', 'M.Tech', 'MCA', 'M.Tech', 'BSc (CS)', 'BSc (CS)', 'MCA', 'BSc (CS)', 'BSc (CS)',
            'BCA', 'MCA', 'B.Tech', 'M.Tech', 'BSc (CS)', 'BCA', 'B.Tech', 'MCA', 'M.Tech', 'BSc (CS)',
            'BCA', 'BCA', 'B.Tech', 'BCA', 'B.Tech', 'MCA', 'MCA', 'M.Tech', 'MCA', 'M.Tech'
        ],
        'Attendance_Percentage': [
            85.0, None, 78.0, 92.0, 65.0, None, 80.0, 88.0, 72.0, 95.0,
            89.0, 74.0, None, 91.0, 68.0, 83.0, None, 79.0, 86.0, 94.0,
            82.0, 77.0, 81.0, 90.0, 69.0, None, 75.0, 87.0, 73.0, 93.0,
            80.0, 84.0, 76.0, 89.0, 67.0, 85.0, 71.0, None, 88.0, 91.0
        ],
        'Mock_Test_Score': [
            '88', '75', 'No Score', '95', '60', '82', '70', '85', '64', '90',
            '84', '72', '79', '91', '63', '87', 'No Score', '76', '81', '93',
            '85', '70', '78', '89', '65', '80', '74', '86', '71', '92',
            '83', '77', '75', '88', '62', '84', '69', '78', '85', '89'
        ]
    }
    
    df = pd.DataFrame(raw_data)
    print("\n[INFO] Large Dataset Created with 40 Records.")
    
    # DATA CLEANING
    mean_attendance = df['Attendance_Percentage'].mean()
    df['Attendance_Percentage'] = df['Attendance_Percentage'].fillna(mean_attendance)
    
    df['Name'] = df['Name'].astype(str).str.strip()
    df['Course'] = df['Course'].astype(str).str.strip()
    
    df['Mock_Test_Score'] = df['Mock_Test_Score'].replace('No Score', '0')
    df['Mock_Test_Score'] = df['Mock_Test_Score'].astype(int)
    df['Attendance_Percentage'] = df['Attendance_Percentage'].round(2)
    
    # Exporting the main dataset for Tableau
    tableau_ready_file = "tableau_ready_dataset.csv"
    df.to_csv(tableau_ready_file, index=False)
    
    print(f"\n[SUCCESS] Cleaned dataset saved to: '{tableau_ready_file}'")
    print("====== Data Preprocessing Successfully Completed ======")

if __name__ == "__main__":
    advanced_large_data_pipeline_clean()