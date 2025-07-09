import pandas as pd

# Since log.csv is in the root folder
df = pd.read_csv("log.csv")

print("\n📋 Visitor Log:")
print(df.to_string(index=False))
