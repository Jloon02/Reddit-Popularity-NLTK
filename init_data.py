import os
import pandas as pd

def assert_file_exists(file_path):
    assert os.path.exists(file_path), f"File not found: {file_path}"

def output_data(comments_folder_path, submissions_folder_path):
    # Check needed data files exists
    try:
        assert_file_exists(comments_folder_path)
        assert_file_exists(submissions_folder_path)
    except AssertionError as e:
        print(e)

    # List of all the .json.gz files in the folder
    comments_json_files = [file for file in os.listdir(comments_folder_path) if file.endswith('.json.gz')]
    submissions_json_files = [file for file in os.listdir(submissions_folder_path) if file.endswith('.json.gz')]

    # Initialize an empty list to store data
    comments_dfs = []
    submissions_dfs = []

    # Loop through each comments .json.gz file and read it into a Pandas DataFrame
    for json_file in comments_json_files:
        comment_file_path = os.path.join(comments_folder_path, json_file)
        
        # Read the compressed JSON file into a DataFrame
        comment_df = pd.read_json(comment_file_path, compression='gzip', lines=True)
        
        # Append the DataFrame to the list
        comments_dfs.append(comment_df)

    # Do the same for submissions
    for json_file in submissions_json_files:
        submission_file_path = os.path.join(submissions_folder_path, json_file)
        
        # Read the compressed JSON file into a DataFrame
        submission_df = pd.read_json(submission_file_path, compression='gzip', lines=True)
        
        # Append the DataFrame to the list
        submissions_dfs.append(submission_df)

    # Concatenate the Dataframes into one
    comments = pd.concat(comments_dfs, ignore_index=True)
    submissions = pd.concat(submissions_dfs, ignore_index=True)

    # Name of the files to output
    comment_file_name = "comments_data.csv"
    submission_file_name = "submissions_data.csv"

    # Output Dataframes into csv files
    comments.to_csv(comment_file_name, encoding='utf-8', index=False)
    submissions.to_csv(submission_file_name, encoding='utf-8', index=False)

    return comment_file_name, submission_file_name