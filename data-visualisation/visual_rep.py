from supabase import create_client, Client
import pandas as pd
import matplotlib.pyplot as plt

url: str = "https://jryeokpjkidbgzscmrcj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpyeWVva3Bqa2lkYmd6c2NtcmNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU5ODQ3NjIsImV4cCI6MjA0MTU2MDc2Mn0.nLeYIrrnbkSVqKeY7XOZkgHxDYwDcQOSVwmzrZgQrMo"

supabase: Client = create_client(url, key)

# Fetch all data from a specific table
response = supabase.table("rating").select("*").execute()

def plot_rubric_statistics_for_user(df, user_id, rubric_columns):
    # Filter the DataFrame to include only the specified user's ratings
    user_df = df[df['user_id'] == user_id]
    
    for rubric in rubric_columns:
        # Get counts of each category in the rubric for this user
        counts = user_df[rubric].value_counts()

        # Plot the data
        plt.figure(figsize=(8, 6))
        counts.plot(kind='bar', color=['red', 'green', 'blue'])
        plt.title(f'Occurrences for {rubric} by User {user_id}')
        plt.xlabel('Response')
        plt.ylabel('Count')
        plt.xticks(rotation=0)
        plt.show()


def plot_combined_rubric_statistics_for_user(df, user_id, rubric_columns):
    # Filter the DataFrame to include only the specified user's ratings
    user_df = df[df['user_id'] == user_id]

    # Prepare a DataFrame to accumulate counts for each rubric
    counts_df = pd.DataFrame()

    # Calculate the counts for each rubric, considering only "Yes" and "No"
    for rubric in rubric_columns:
        counts = user_df[rubric].value_counts()
        # Filter to include only "Yes" and "No"
        counts = counts[counts.index.isin(['Yes', 'No'])]
        counts_df[rubric] = counts

    # Transpose the DataFrame for easier plotting
    counts_df = counts_df.T

    # Plot the combined results
    counts_df.plot(kind='bar', figsize=(12, 8), color=['#1f77b4', '#ff7f0e'])
    plt.title(f'Combined Occurrences of Yes and No for All Rubrics by User 01')
    plt.xlabel('Rubric')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Response')
    plt.tight_layout()
    plt.show()


def plot_rubric_statistics(df, rubric):
    # Get counts of each category in the rubric across all users
    counts = df[rubric].value_counts()

    # Plot the data
    plt.figure(figsize=(8, 6))
    counts.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.title(f'Occurrences for {rubric} Across All Users')
    plt.xlabel('Response')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

# Check if the request was successful
if hasattr(response, 'status_code') and response.status_code != 200:
    print(f"Error fetching data: {response.status_code}")
    # Check if there's additional error information
    if hasattr(response, 'data') and 'message' in response.data:
        print(f"Error message: {response.data['message']}")
else:
    # Convert the data to a Pandas DataFrame
    data = response.data
    df = pd.DataFrame(data)
    # Display the DataFrame
    print(df)

    # Call the function for rubric_2
    plot_combined_rubric_statistics_for_user(df, '7d8591de-831f-44df-81d1-24dfb0ea1d10', ['rubric_1', 'rubric_2', 'rubric_3', 'rubric_4', 'rubric_5'])







