import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:

    # Create the 'bonus' column with doubled salary values
    employees['bonus'] = employees['salary'] * 2
    
    return employees

# Example usage
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'salary': [5000, 6000, 7000]
}

employees_df = pd.DataFrame(data)
updated_employees_df = createBonusColumn(employees_df)
print(updated_employees_df)
