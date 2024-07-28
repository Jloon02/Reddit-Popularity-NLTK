import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def read_data(comPath, subPath):
    comments = pd.read_csv(comPath)        # comments DF
    submissions = pd.read_csv(subPath)     # submissions DF

    # Select relevant features
    selected_features = ['archived', 'created_utc', 'downs', 'edited', 'gilded', 'hide_score', 'is_self', 'num_comments',
                          'over_18', 'quarantine', 'saved', 'selftext', 'subreddit', 'stickied', 'thumbnail', 'title', 
                          'ups', 'url', 'year', 'month', 'link_flair_css_class', 'link_flair_text', 'author_flair_css_class', 
                          'author_flair_text', 'distinguished', 'media', 'secure_media']
    popular_features = 'score'

    # Extract features and target variable
    X = submissions[selected_features].copy()
    y = submissions[popular_features].copy()

    # Convert boolean features to numerical using Label Encoding
    boolean_features = ['archived', 'edited', 'hide_score', 'is_self', 'over_18', 'quarantine', 'saved', 'stickied']
    for feature in boolean_features:
        X[feature] = LabelEncoder().fit_transform(X[feature])

    # Convert string features to numerical using Label Encoding
    string_features = ['subreddit', 'thumbnail', 'title', 'url',
                    'link_flair_css_class', 'link_flair_text', 'author_flair_css_class',
                    'author_flair_text', 'distinguished', 'media', 'secure_media', 'selftext']
    for feature in string_features:
        X[feature] = LabelEncoder().fit_transform(X[feature])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instantiate the RandomForestClassifier
    rf_classifier = RandomForestClassifier(random_state=42)

    # Train the model
    rf_classifier.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = rf_classifier.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy for Importance Prediction: {accuracy}')

    # Display feature importances
    feature_importances = pd.DataFrame({'Feature': selected_features, 'Importance': rf_classifier.feature_importances_})

    # Only get the features over the limit of importance
    IMPORTANCE = 0.05
    important_features = feature_importances[feature_importances['Importance'] >= IMPORTANCE]

    # Keep only the features we need
    submission_score = submissions[['score', 'permalink']]
    submissions = submissions[important_features['Feature'].transpose()]
    submissions_merged = pd.concat([submission_score, submissions], axis=1)

    return comments, submissions_merged