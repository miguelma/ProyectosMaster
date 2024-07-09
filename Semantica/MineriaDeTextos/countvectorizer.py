from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=True)
corpus = ["Esto", "Esto"]
X = vectorizer.fit_transform(corpus)
print(X.toarray()) # [[0.], [0.]]
