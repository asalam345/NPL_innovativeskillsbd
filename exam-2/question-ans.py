import PyPDF2
import re
# import nltk
# from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

cv1 = extract_text("exam_cv.pdf")
cv2 = extract_text("Rafi_Mehebub_Bhuiyan_CV.pdf")
cv3 = extract_text("Sm_Nuruzzaman_Nobel.pdf")

#stop_words = set(stopwords.words("english"))

# def clean_text(text):
#     text = text.lower()
#     text = re.sub(r'[^a-z\s]', '', text)
#     words = text.split()
#     words = [w for w in words if w not in stop_words]
#     return " ".join(words)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text
#ans 2
cv1_clean = clean_text(cv1)
cv2_clean = clean_text(cv2)
cv3_clean = clean_text(cv3)
# print('cv1_clean: ')
# print(cv1_clean)
# print('cv2_clean: ')
# print(cv2_clean)
# print('cv3_clean: ')
# print(cv3_clean)
# print('online job: ')
# print(oj)

#ans 3

oj = extract_text("online-job.pdf")

cv_documents = [cv1_clean, cv2_clean, cv3_clean, oj]

#ans -4,5
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(cv_documents)


#ans-6

similarity = cosine_similarity(tfidf_matrix)

#ans-7
job_similarity = similarity[-1][0:3]
print(job_similarity)

#ans-8
scores = pd.DataFrame({
    "CV": ["CV1", "CV2", "CV3"],
    "Similarity Score": job_similarity
})

ranking = scores.sort_values(by="Similarity Score", ascending=False)
print(ranking)