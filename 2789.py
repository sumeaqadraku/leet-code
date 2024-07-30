import pandas as pd
from typing import List

data = {
    'employee_id': [3,2,3,4,5,6],
    'name': ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan", "Khaled"],
    'department': ["Operations", "Sales", "Engineering", "IT", "HR", "Administration"],
    'salary': [5334, 4433, 3322, 2221, 8888, 2222]
}
df = pd.DataFrame(data)
    
first_three_rows = df.head(3)
print(first_three_rows)
    
    