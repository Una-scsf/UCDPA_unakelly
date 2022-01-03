import pandas as pd
prospects = pd.read_csv("/Users/ukelly/Desktop/UCDPA_una/Prospects_January_2022.csv")
print(prospects.head())
print(prospects.info())

ordered_prospects = prospects.sort_values("Score", ascending=False)

print(ordered_prospects["Email"].value_counts(sort=True))

ordered_prospects.drop_duplicates(subset="Email")

print(ordered_prospects.isna().any())

import matplotlib.pyplot as plt
ordered_prospects.isna().sum().plot(kind="bar", rot = 45, title = "Columns with Missing Values")
plt.show()
plt.clf()

ordered_prospects["Grade"].fillna("D", inplace=True)

ordered_prospects.isna().sum().plot(kind="bar", rot = 45, title = "Updated Columns with Missing Values")
plt.show()
plt.clf()

ordered_prospects["Full Name"] = ordered_prospects["First Name"] + " " + ordered_prospects["Last Name"]
print(ordered_prospects)