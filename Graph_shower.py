import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('today_menu.csv')
students_df = pd.read_csv('students.csv')

# Identify soup rows if any
soup_rows = df[df['number'].astype(str).str.lower() == 'soup']
main_rows = df[df['number'].astype(str).str.lower() != 'soup']

# Convert numeric columns safely
for col in ['orders', 'price', 'combo']:
    main_rows.loc[:, col] = pd.to_numeric(main_rows[col], errors='coerce').fillna(0)

# 📊 Bar chart: Lunch orders per person
plt.figure(figsize=(10, 6))
sns.barplot(x='lunch', y='orders', data=main_rows, palette='coolwarm', legend=False)
plt.title('Lunch Orders per Person')
plt.xlabel('Lunch Item')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🥧 Pie chart: Lunch participation using total student count
total_students = len(students_df)
print(len(students_df))
students_who_ordered = main_rows['orders'].gt(0).sum()
students_who_did_not_order = total_students - students_who_ordered

# Pie chart data
participation_data = [students_who_ordered, students_who_did_not_order]
labels = ['Ordered Lunch', 'Did Not Order']
colors = ['lightgreen', 'lightcoral']

plt.figure(figsize=(6, 6))
plt.pie(participation_data, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title(f'Lunch Participation (Total Students: {total_students})')
plt.tight_layout()
plt.show()


# 💰 Revenue Summary
lunch_revenue = (main_rows['orders'] * main_rows['price']).sum()
combo_revenue = (main_rows['orders'] * main_rows['combo']).sum()
soup_revenue = (pd.to_numeric(soup_rows['orders'], errors='coerce').fillna(0) * pd.to_numeric(soup_rows['price'], errors='coerce').fillna(0)).sum()
total_revenue = lunch_revenue + combo_revenue + soup_revenue

print(f"🍱 Lunch Revenue: HK${lunch_revenue:.2f}")
print(f"🥤 Combo Revenue: HK${combo_revenue:.2f}")
print(f"🍲 Soup Revenue: HK${soup_revenue:.2f}")
print(f"💵 Total Revenue: HK${total_revenue:.2f}")
