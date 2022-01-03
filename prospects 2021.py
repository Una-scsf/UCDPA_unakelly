import pandas as pd
prospects = pd.read_csv("/Users/ukelly/Desktop/UCDPA_una/Prospects_January_2022.csv")
print(prospects.head())
print(prospects.info())

prospects["Full Name"] = prospects["First Name"] + " " + prospects["Last Name"]

dup_prospects = prospects.sort_values("Score", ascending=False)

print(dup_prospects["Email"].value_counts(sort=True))

unq_prospects = dup_prospects.drop_duplicates(subset="Email")

print(unq_prospects.isna().any())

import matplotlib.pyplot as plt
unq_prospects.isna().sum().plot(kind="bar", rot = 45, title = "Columns with Missing Values")
plt.show()
plt.clf()

unq_prospects["Grade"].fillna("D", inplace=True)

unq_prospects.isna().sum().plot(kind="bar", rot = 45, title = "Updated Columns with Missing Values")
plt.show()
plt.clf()

print(unq_prospects)

hot_prospects = pd.read_csv("/Users/ukelly/Desktop/UCDPA_una/Hot_Prospects_2022.csv")
unq_with_hot_prospects = pd.merge(unq_prospects, hot_prospects, on=["Prospect Id", "Email"], how="outer")

unq_with_hot_prospects["Last Activity Date"] = pd.to_datetime((unq_with_hot_prospects["Last Activity Date"]))
unq_with_hot_prospects["Created Date"] = pd.to_datetime((unq_with_hot_prospects["Created Date"]))

print(unq_with_hot_prospects.info())