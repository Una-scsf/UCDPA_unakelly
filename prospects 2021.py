import pandas as pd
prospects = pd.read_csv("/Users/ukelly/Desktop/UCDPA_unakelly/Prospects_January_2022.csv")
print(prospects.head())
print(prospects.info())

prospects["Last Activity Date"] = pd.to_datetime((prospects["Last Activity Date"]))
prospects["Created Date"] = pd.to_datetime((prospects["Created Date"]))
prospects["First Name"] = prospects["First Name"].str.capitalize()
prospects["Last Name"] = prospects["Last Name"].str.capitalize()
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

hot_prospects = pd.read_csv("/Users/ukelly/Desktop/UCDPA_unakelly/Hot_Prospects_2022.csv")
unq_with_hot_prospects = pd.merge(unq_prospects, hot_prospects, on=["Prospect Id", "Email"], how="outer")

unq_with_hot_prospects.reset_index()

print(unq_with_hot_prospects.info())

fig, ax = plt.subplots()
ax.hist(unq_with_hot_prospects["Lifecycle Stage"], bins=6, color="green", edgecolor="black")
ax.set_xlabel("Lifecycle Stage")
ax.set_ylabel("# of customers")
ax.set_title("Lifecycle stage of customers")
plt.show()

a_plus_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "A+"].count()[0]
a_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "A"].count()[0]
a_minus_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "A-"].count()[0]
b_plus_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "B+"].count()[0]
b_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "B"].count()[0]
b_minus_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "B-"].count()[0]
c_plus_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "C+"].count()[0]
c_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "C"].count()[0]
c_minus_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "C-"].count()[0]
d_plus_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "D+"].count()[0]
d_grade = unq_with_hot_prospects.loc[unq_with_hot_prospects["Grade"] == "D"].count()[0]

labels = ["A+", "A", "B+", "B", "B-", "C+", "C-", "D" ] #not A-, C, D+ included in graph, 0 matches

fig, ax = plt.subplots()
ax.pie([a_plus_grade, a_grade, b_plus_grade, b_grade, b_minus_grade, c_plus_grade, c_minus_grade, d_grade], labels=labels, autopct="%.0f %%")
plt.title("Grade of customers")
plt.show()

fig, ax = plt.subplots()
ax.hist(unq_with_hot_prospects["Score"], bins=[100,200,300,400,500,600,700,800,900], orientation="horizontal", color="purple", edgecolor="black")
ax.set_xlabel("# of customers")
ax.set_ylabel("Score")
ax.set_title("Engagement score of customers")
plt.show()