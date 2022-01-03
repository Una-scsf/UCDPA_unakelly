import pandas as pd
prospects = pd.read_csv("/Users/ukelly/Desktop/UCDPA_una/Prospects_January_2022.csv")
print(prospects.head())
print(prospects.info())

prospects.sort_values("Score", ascending=False)

print(prospects["Email"].value_counts())
print(prospects.isna().any())

prospects.drop_duplicates(subset="Email")

import matplotlib.pyplot as plt
prospects.isna().sum().plot(kind="bar", rot = 45, title = "Columns with Missing Values")
plt.show()
plt.clf()