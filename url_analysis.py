import pandas
import seaborn
import matplotlib.pyplot as plt

def plot_url(dataframe):
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

    # First subplot - including rows with 0 scores
    seaborn.barplot(x='urlexists', y='score', data=dataframe, estimator='mean', ax=axes[0], errorbar=None)
    axes[0].set_xlabel('urlexists')
    axes[0].set_ylabel('Average Score')
    axes[0].set_title('Average Scores for urlexists=True and urlexists=False (including 0 scores)')

    # Second subplot - excluding rows with 0 scores
    dataframe_no_zero = dataframe[dataframe['score'] != 0]
    seaborn.barplot(x='urlexists', y='score', data=dataframe_no_zero, estimator='mean', ax=axes[1], errorbar=None)
    axes[1].set_xlabel('urlexists')
    axes[1].set_ylabel('Average Score')
    axes[1].set_title('Average Scores for urlexists=True and urlexists=False (excluding 0 scores)')

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.savefig('avg_url_scores_withandwithout_zeros')
    plt.clf()
    plt.cla()

def analyze_url(dataframe):
    # if the permalink is contained in the url column, then that means that post didn't have a url
    # make a new column "urlexists"
    dataframe['urlexists'] = dataframe.apply(lambda row: False if row['url'].find(row['permalink']) != -1 else True, axis=1)
    plot_url(dataframe)
