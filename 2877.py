import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Creating the DataFrame
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# Example 2D list of student data
student_data = [
    [1, 18],
    [2, 19],
    [3, 20],
    [4, 21],
    [5, 22]
]

df = createDataframe(student_data)


print(df)
