from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(stop_words=["este", "algunas"])
text = ["Este es un ejemplo de texto con algunas palabras vacías."]
vectors = vectorizer.fit_transform(text)
print(vectorizer.get_feature_names()) #_out
