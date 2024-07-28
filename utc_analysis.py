import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone

def plot_utc(average_score):
    # Plotting
    plt.bar(average_score.index, average_score.values, color='skyblue', label='Average Score')

    # Adding labels and title
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Score')
    plt.title('What hour in the day gives the highest score?')
    plt.xticks(range(24))  # Assuming 24 hours in a day

    # Find and mark the time of day with the highest average score
    max_avg_score_time = average_score.idxmax()
    plt.axvline(x=max_avg_score_time, color='red', linewidth=5, linestyle='--', label=f'Max Time of Day ({max_avg_score_time})')

    # Add legend
    plt.legend()
    plt.savefig('UTC_score_results')
    plt.clf()
    plt.cla()

def init(submission_df):
    # Change utc to date time format
    submission_df['timestamp'] = pd.to_datetime(submission_df['created_utc'], unit='s', utc=True)
    
    # Extract the time of the day
    submission_df['hour_of_day'] = submission_df['timestamp'].dt.hour

    # Group by 'hour_of_day' and calculate the average score for each group
    average_scores = submission_df.groupby('hour_of_day')['score'].mean()

    # Plot the graph
    plot_utc(average_scores)