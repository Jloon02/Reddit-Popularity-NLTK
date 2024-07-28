import init_data
import read_data
import utc_analysis
import url_analysis
import title_analysis

def main():
    # File locations
    comment_file_path = 'comments'
    submissions_file_path = 'submissions'

    # Path to the folder containing the .json.gz files
    comment_file, submission_file = init_data.output_data(comment_file_path, submissions_file_path)

    comment_file = 'comments_data.csv'
    submission_file = 'submissions_data.csv'
    _, submissions_df = read_data.read_data(comment_file, submission_file)

    url_analysis.analyze_url(submissions_df)
    utc_analysis.init(submissions_df)
    title_analysis.analyze_title(submissions_df)

if __name__ == "__main__":
    main()