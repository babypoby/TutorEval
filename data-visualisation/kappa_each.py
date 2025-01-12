import matplotlib.pyplot as plt
from supabase import create_client, Client
from collections import defaultdict

url: str = "https://jryeokpjkidbgzscmrcj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpyeWVva3Bqa2lkYmd6c2NtcmNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU5ODQ3NjIsImV4cCI6MjA0MTU2MDc2Mn0.nLeYIrrnbkSVqKeY7XOZkgHxDYwDcQOSVwmzrZgQrMo"

supabase: Client = create_client(url, key)
ratings_response = supabase.table("rating").select("conversation_id, rubric_1, rubric_2, rubric_4, rubric_5, user_id").execute()
ratings_data = ratings_response.data

target_user_id = "7d8591de-831f-44df-81d1-24dfb0ea1d10"
all_users = []

for record in ratings_data:
    if (record['user_id'] != target_user_id) & (record['user_id'] not in all_users):
        all_users.append(record['user_id'])

rubrics = ['rubric_1', 'rubric_2', 'rubric_4', 'rubric_5']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Assign different colors to each rubric

# To hold data points for each rubric
data_points = {rubric: {'conversation_counts': [], 'kappa_values': []} for rubric in rubrics}

# To hold user_ids with kappa below threshold for each rubric
low_kappa_users = {rubric: [] for rubric in rubrics}

for rubric, color in zip(rubrics, colors):
    for user in all_users:
        contingency_table = {
            'Yes': {'Yes': 0, 'No': 0, 'Not Applicable': 0},
            'No': {'Yes': 0, 'No': 0, 'Not Applicable': 0},
            'Not Applicable': {'Yes': 0, 'No': 0, 'Not Applicable': 0}
        }

        grouped_ratings = defaultdict(list)
        for record in ratings_data:
            if record['user_id'] == user or record['user_id'] == target_user_id:
                conversation_id = record['conversation_id']
                value = record.get(rubric)
                grouped_ratings[conversation_id].append(value)

        n_conversations = 0
        for conv_id, ratings in grouped_ratings.items():
            if len(ratings) == 2:  
                n_conversations += 1
                target_rating = None
                other_rating = None
                
                for record in ratings_data:
                    if record['conversation_id'] == conv_id:
                        if record['user_id'] == target_user_id:
                            target_rating = record.get(rubric)
                        elif record['user_id'] == user:
                            other_rating = record.get(rubric)
                
                if target_rating and other_rating:
                    contingency_table[target_rating][other_rating] += 1

        n = sum(sum(row.values()) for row in contingency_table.values())
        if n == 0:
            continue
        
        p_o = (
            contingency_table['Yes']['Yes'] +
            contingency_table['No']['No'] +
            contingency_table['Not Applicable']['Not Applicable']
        ) / n

        p_target_yes = sum(contingency_table['Yes'].values()) / n
        p_target_no = sum(contingency_table['No'].values()) / n
        p_target_na = sum(contingency_table['Not Applicable'].values()) / n

        p_other_yes = (
            contingency_table['Yes']['Yes'] +
            contingency_table['No']['Yes'] +
            contingency_table['Not Applicable']['Yes']
        ) / n
        p_other_no = (
            contingency_table['Yes']['No'] +
            contingency_table['No']['No'] +
            contingency_table['Not Applicable']['No']
        ) / n
        p_other_na = (
            contingency_table['Yes']['Not Applicable'] +
            contingency_table['No']['Not Applicable'] +
            contingency_table['Not Applicable']['Not Applicable']
        ) / n

        p_e = (
            p_target_yes * p_other_yes +
            p_target_no * p_other_no +
            p_target_na * p_other_na
        )

        kappa = (p_o - p_e) / (1 - p_e) if p_e != 1 else 1

        data_points[rubric]['conversation_counts'].append(n_conversations)
        data_points[rubric]['kappa_values'].append(kappa)

        # Check and store the user_id if kappa is below 0.4
        if kappa <= 0.4:
            low_kappa_users[rubric].append(user)

rubrics_labels = {
    'rubric_1': 'Do not reveal the answer',
    'rubric_2': 'Promote active engagement',
    'rubric_4': 'Communicate with positive tone',
    'rubric_5': 'Identify and address misconceptions'
}

# Plotting section
plt.figure(figsize=(10, 6))
for rubric, color in zip(rubrics, colors):
    plt.scatter(data_points[rubric]['conversation_counts'], 
                data_points[rubric]['kappa_values'], 
                color=color, 
                label=rubrics_labels[rubric])

plt.title("Cohen's Kappa vs. Number of Conversations Rated for Different Rubrics")
plt.xlabel("Number of Conversations")
plt.ylabel("Cohen's Kappa")
plt.legend()
plt.grid(True)
plt.show()

# Output users with low kappa
for rubric, users in low_kappa_users.items():
    if users:
        print(f"Rubric '{rubrics_labels[rubric]}' - Users with Kappa below 0.4: {', '.join(users)}")

