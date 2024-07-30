import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Select the name and age of the student with student_id = 101.
    
    Parameters:
    - students: pd.DataFrame - The DataFrame containing student data.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the name and age of the student with student_id = 101.
    """
    # Filter the DataFrame for the student with the specified student_id
    student_info = students[students['student_id'] == 101]
    
    # Check if the filtered DataFrame is not empty
    if not student_info.empty:
        # Select the 'name' and 'age' columns
        result = student_info[['name', 'age']]
    else:
        # Return an empty DataFrame with the expected columns if no match is found
        result = pd.DataFrame(columns=['name', 'age'])
    
    return result

# Example usage
data = {
    'student_id': [101, 53, 128, 3],
    'name': ["Ulysses", "William", "Henry", "Henry"],
    'age': [13, 10, 6, 11]
}

students_df = pd.DataFrame(data)
selected_student = selectData(students_df)
print(selected_student)
