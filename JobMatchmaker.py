from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from utils import preprocessor

class JobMatchmaker():
    def __init__(self, data_path):
        self.vectorizer = TfidfVectorizer(max_features=10000, max_df=0.5, min_df=5, preprocessor=preprocessor)

        jd = []
        with open(f'{data_path}/training.txt', 'r') as f:
            for line in f.readlines():
                jd.append(line)

        self.jd_vec = self.vectorizer.fit_transform(jd)
        self.neigh = NearestNeighbors()
        self.neigh.fit(self.jd_vec)

        self.df = pd.read_csv(f'{data_path}/job_post.csv')

    def get_match_job(self, resume, num_jobs):
        resume_vec = self.vectorizer.transform([resume])
        _, index = self.neigh.kneighbors(resume_vec, n_neighbors=num_jobs)
        index = index.flatten()
        # print(self.df)
        return self.df.iloc[index]