from supabase import create_client, Client
from collections import defaultdict
import pandas as pd

url: str = "https://jryeokpjkidbgzscmrcj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpyeWVva3Bqa2lkYmd6c2NtcmNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU5ODQ3NjIsImV4cCI6MjA0MTU2MDc2Mn0.nLeYIrrnbkSVqKeY7XOZkgHxDYwDcQOSVwmzrZgQrMo"

supabase: Client = create_client(url, key)
ratings_response = supabase.table("rating").select("conversation_id, rubric_1, user_id").execute()
ratings_data = ratings_response.data

# Define target user ID
target_user_id = "7d8591de-831f-44df-81d1-24dfb0ea1d10"

# Create contingency table
contingency_table = {
    'Yes': {'Yes': 0, 'No': 0, 'Not Applicable': 0},
    'No': {'Yes': 0, 'No': 0, 'Not Applicable': 0},
    'Not Applicable': {'Yes': 0, 'No': 0, 'Not Applicable': 0}
}

# Group ratings by conversation_id
conversation_ratings = defaultdict(dict)
for record in ratings_data:
    conversation_id = record['conversation_id']
    user_id = record['user_id']
    rating = record['rubric_1']
    conversation_ratings[conversation_id][user_id] = rating

# Fill contingency table
for conv_ratings in conversation_ratings.values():
    if target_user_id in conv_ratings and len(conv_ratings) > 1:
        target_rating = conv_ratings[target_user_id]
        # Get the other user's rating (first non-target user found)
        other_rating = next(rating for user_id, rating in conv_ratings.items() if user_id != target_user_id)
        print(f"Target: {target_rating}, Other: {other_rating}")
        print(f"conversation_id: {conv_ratings}")
        contingency_table[target_rating][other_rating] += 1

# Print contingency table
print("\nContingency Table:")
print("                Other Rater")
print("Target Rater    Yes    No    Not Applicable")
for rating1 in ['Yes', 'No', 'Not Applicable']:
    print(f"{rating1:<12} {contingency_table[rating1]['Yes']:<6} {contingency_table[rating1]['No']:<6} {contingency_table[rating1]['Not Applicable']:<6}")

# Calculate totals
n = sum(sum(row.values()) for row in contingency_table.values())

# Calculate observed agreement (p_o)
p_o = (contingency_table['Yes']['Yes'] + 
       contingency_table['No']['No'] + 
       contingency_table['Not Applicable']['Not Applicable']) / n

# Calculate marginal proportions
p_target_yes = sum(contingency_table['Yes'].values()) / n
p_target_no = sum(contingency_table['No'].values()) / n
p_target_na = sum(contingency_table['Not Applicable'].values()) / n

p_other_yes = (contingency_table['Yes']['Yes'] + 
               contingency_table['No']['Yes'] + 
               contingency_table['Not Applicable']['Yes']) / n
p_other_no = (contingency_table['Yes']['No'] + 
              contingency_table['No']['No'] + 
              contingency_table['Not Applicable']['No']) / n
p_other_na = (contingency_table['Yes']['Not Applicable'] + 
              contingency_table['No']['Not Applicable'] + 
              contingency_table['Not Applicable']['Not Applicable']) / n

# Calculate expected agreement (p_e)
p_e = (p_target_yes * p_other_yes + 
       p_target_no * p_other_no + 
       p_target_na * p_other_na)

# Calculate Cohen's Kappa
kappa = (p_o - p_e) / (1 - p_e) if p_e != 1 else 1

print(f"\nTotal conversations: {n}")
print(f"Observed agreement (p_o): {p_o:.3f}")
print(f"Expected agreement (p_e): {p_e:.3f}")
print(f"Cohen's Kappa: {kappa:.3f}")
