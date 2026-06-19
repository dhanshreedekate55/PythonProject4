import numpy as np
records = [(1, 'Alice', 25.5),(2, 'Bob', 30.5), (3,'Charlie', 28.0)]
dtype = [('id', 'i4'), ('name', 'U10'), ('age', 'f4')]
structured_array = np.fromrecords(records, dtype=dtype)
print(structured_array['name'])
print(structured_array['age'])