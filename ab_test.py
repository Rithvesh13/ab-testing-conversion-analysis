import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- A/B Test Analysis Started ---")

# 1. LOAD DATA
# Reading the CSV file
try:
    df = pd.read_csv("ab_data.csv")
    print("Data loaded successfully.")
    print(f"Total rows in raw data: {len(df)}")
except FileNotFoundError:
    print("ERROR: File not found.")
    print("Make sure 'ab_data.csv' is in C:\\Users\\Rithvesh\\")
    exit()

# 2. CLEAN DATA
# Find rows where group and landing page don't match
mismatch = df[((df['group'] == 'treatment') & (df['landing_page'] == 'old_page')) | 
              ((df['group'] == 'control') & (df['landing_page'] == 'new_page'))]

# Remove bad rows
df_clean = df[~df.index.isin(mismatch.index)]

# Remove duplicate users
df_clean = df_clean.drop_duplicates(subset='user_id')

print(f"Data cleaned. Remaining rows: {len(df_clean)}")

# 3. CALCULATE CONVERSION RATES
# Separate the groups
control = df_clean[df_clean['group'] == 'control']
treatment = df_clean[df_clean['group'] == 'treatment']

# Calculate mean (conversion rate)
p_control = control['converted'].mean()
p_treatment = treatment['converted'].mean()

print("\n--- Conversion Rates ---")
print(f"Control Group (Old Page):   {p_control:.2%}")
print(f"Treatment Group (New Page): {p_treatment:.2%}")

# 4. Z-TEST (Statistics)
# Get counts
n_control = len(control)
n_treatment = len(treatment)
x_control = control['converted'].sum()
x_treatment = treatment['converted'].sum()

# Pooled Probability
p_pool = (x_control + x_treatment) / (n_control + n_treatment)

# Standard Error
se = np.sqrt(p_pool * (1 - p_pool) * (1/n_control + 1/n_treatment))

# Z-Score
diff = p_treatment - p_control
z_score = diff / se

print("\n--- Statistical Test ---")
print(f"Z-Score: {z_score:.4f}")

# 5. FINAL DECISION
print("\n--- FINAL CONCLUSION ---")
if z_score > 1.96:
    print("SIGNIFICANT! The New Page is better. LAUNCH IT.")
elif z_score < -1.96:
    print("SIGNIFICANT! The New Page is worse. DO NOT LAUNCH.")
else:
    print("NOT SIGNIFICANT. The difference is just luck. KEEP OLD PAGE.")

# 6. VISUALIZATION (Matplotlib)
print("\nGenerating Chart...")

# Data for chart
groups = ['Control\n(Old Page)', 'Treatment\n(New Page)']
rates = [p_control, p_treatment]

# Create bar chart
plt.figure(figsize=(6, 5))
bars = plt.bar(groups, rates, color=['blue', 'orange'])
plt.title('A/B Test: Conversion Rate Comparison')
plt.ylabel('Conversion Rate')
plt.ylim(0, 0.15)  # Set y-axis limit to make differences visible

# Add percentage labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.002,
             f'{height:.2%}', ha='center', va='bottom', fontweight='bold')

plt.show()
