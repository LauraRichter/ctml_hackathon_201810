# Create fake data files for submission, for benchmarking

import pandas as pd
import numpy as np

df_submit = pd.read_csv('Devex_submission_format.csv', encoding="ISO-8859-1")
df_submit = df_submit.set_index('ID')

# All zeros
df_submit_0 = df_submit * 0.
df_submit_0.fillna(0, inplace=True)
df_submit_0.astype(int).to_csv('benchmark_0.csv')

# All ones
df_submit_1 = df_submit_0 + 1.
df_submit_1.astype(int).to_csv('benchmark_1.csv')

# Random
df_submit_random = df_submit_0 + np.random.randint(0, 2, size=df_submit.shape)
df_submit_random.astype(int).to_csv('benchmark_random.csv')
