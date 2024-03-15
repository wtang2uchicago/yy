# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('hello Chicago')


import matplotlib.pyplot as plt

# Data
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
males = [64.6, 65.5, 65.4, 64.9, 65.4, 65.6, 65.2, 64.8, 64.1, 64.4, 64.6]
females = [35.4, 34.5, 34.6, 35.1, 34.6, 34.4, 34.8, 35.2, 35.9, 35.6, 35.4]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(years, males, marker='o', label='Males')
plt.plot(years, females, marker='o', label='Females')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Percentage of Males and Females in Management Occupations (2012-2022)')
plt.legend()

# Show plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

# Data
provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', 'New Brunswick']
expenditure = [18323.00, 5400.00, 34527.00, 26515.00]

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(provinces, expenditure, color='skyblue')
plt.xlabel('Expenditure (Dollars)')
plt.ylabel('Provinces')
plt.title('Household Final Consumption Expenditure Estimates by Province (2021)')
plt.gca().invert_yaxis()  # Invert y-axis to display provinces from top to bottom
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Add grid lines
plt.tight_layout()

# Display the plot
plt.show()
