from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

vectorizer = TfidfVectorizer()
jd_vec = vectorizer.fit_transform(jd)
resume_vec = vectorizer.transform(resume)

neigh = NearestNeighbors(n_neighbors=2)
neigh.fit(jd_vec)

neigh.kneighbors(resume_vec)