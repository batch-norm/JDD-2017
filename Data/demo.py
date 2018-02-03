

import pandas as pd
import numpy as np

# d1 = pd.DataFrame({
#     'id':[1,2,4,6,8,10],
#     'value':[np.nan,1,1,4,6,np.nan]
# })
# print(d1)
# d2 = pd.DataFrame({
#     'id':[1,10],
#     'value':[1,1]
# })
# print(d2)
# print(d1.update(d2))
df = pd.DataFrame({'A': ['a', 'b', 'c'],
                    'B': ['x', 'y', 'z']})
print(df)
new_df = pd.DataFrame({'B': ['d', 'e', 'f', 'g', 'h', 'i']})
print(new_df)
df.update(new_df)
print(df)