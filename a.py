import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')  # Download the stop words if not already downloaded

# Get the list of English stop words
stop_words = set(stopwords.words('english'))

print(f"Number of stop words in NLTK: {len(stop_words)}")
print("Some examples of stop words:", list(stop_words))

