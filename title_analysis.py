import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def analyze_title(data):
    # Download the stopwords resource
    nltk.download('stopwords')
    nltk.download('punkt')

    # Preprocess the text data
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    def preprocess_text(text):
        words = word_tokenize(text)
        words = [ps.stem(word.lower()) for word in words if word.isalpha() and word.lower() not in stop_words]
        return ' '.join(words)

    data['Processed_Title'] = data['title'].apply(preprocess_text)

    # Vectorize the processed titles
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['Processed_Title'])
    y = data['score']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple Naive Bayes model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Predict scores on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy for Title Prediction: {accuracy}")

    # Get the most important words/features
    feature_names = vectorizer.get_feature_names_out()
    coef = model.feature_log_prob_[0]

    # Map feature names to their coefficients
    word_coef = dict(zip(feature_names, coef))

    # Sort the words based on their coefficients
    sorted_word_coef = sorted(word_coef.items(), key=lambda x: x[1], reverse=True)

    # Specify the file path
    output_file_path = 'top_words_title.txt'

    # Open the file in write mode
    with open(output_file_path, 'w') as file:
        # Write the header
        file.write("Rank\tWord\n")

        # Write the top words and their rankings to the file
        for rank, (word, _) in enumerate(sorted_word_coef[:25], start=1):  # Change 5 to the desired number of top words
            file.write(f"{rank}\t{word}\n")

    print(f"Top words and rankings written to: {output_file_path}")