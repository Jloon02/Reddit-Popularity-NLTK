# Reddit Popularity Analysis

## 📈 What Makes a Reddit Post Popular?

This project explores the factors that contribute to the popularity of Reddit posts by analyzing patterns in content, timing, and structure. The goal is to determine which features most significantly impact post scores and how to leverage these insights to "farm karma."

---

## 🔍 Project Overview


Developed a data-driven Python application to analyze over **6.5 million Reddit posts**, focusing on key variables such as title structure, time of posting, and presence of URLs. Using **Spark**, **NLTK**, and **Scikit-learn**, we built a machine learning pipeline that predicts post popularity with **86% accuracy**.

---

## 🧠 Key Questions Explored

- What features correlate with high-scoring Reddit posts?
- How does timing or structure influence popularity?
- Can we manipulate specific features to increase post score?

---

## 🛠️ Tech Stack

- **Languages**: Python  
- **Libraries**: Spark, Numpy, Pandas, Scikit-learn, NLTK, Seaborn, Matplotlib  
- **Tools**: GitHub, Jupyter, Terminal  
- **ML Model**: Naïve Bayes Classifier (NLTK-based)  

---

## 📂 Project Structure

To run the application:

**python popularity_prediction.py**

No arguments are required. Just ensure that the **Reddit comments and submissions data files** are in the same directory.

### 🔁 Order of Execution

The program sequentially runs the following modules:

1. `init_data.py` – Initializes and configures the dataset  
2. `read_data.py` – Reads and pre-processes submissions/comments  
3. `url_analysis.py` – Analyzes impact of URLs in posts  
4. `utc_analysis.py` – Examines score trends by posting hour  
5. `title_analysis.py` – NLP analysis on post titles using NLTK  

---

## 📊 Output Files

- **`avg_url_score_withandwithout_zeros.png`**  
  Visualizes the average post score with and without a URL in the body.

- **`UTC_score_results.png`**  
  Shows average post score distribution by UTC hour of submission.

- **`top_words_title.txt`**  
  Lists the top 25 title words most associated with high scores.

---

## 📥 Expected Input

- Reddit comments and submissions data files (`.csv` or `.json` as expected by the scripts)

## 📤 Expected Output

- `.png` and `.txt` files with analytical insights and results

---

## 🧾 Requirements

All dependencies are listed in the `requirements.txt` file.

To install them, run:

```bash
pip install -r requirements.txt
```    


_Note: You may need to run the following once to download required NLTK packages:_

```python
import nltk  
nltk.download('stopwords')  
nltk.download('punkt')  
```

## 🧾 Additional Notes

- The features score and ups were found to be equivalent and thus, one was excluded.

- Several unrelated columns were discarded to streamline the analysis.