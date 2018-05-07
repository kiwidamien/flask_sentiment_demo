import cPickle as pickle

naive_bayes = pickle.load(open('./train_set/naivebayes.pkl'))
vectorizer  = pickle.load(open('./train_set/vectorizer.pkl'))

def vectorize_review(review_text):
    return vectorizer.transform([review_text])

def make_hard_prediction(review_text):
    return naive_bayes.predict(vectorize_review(review_text))

def make_soft_prediction(review_text):
    return naive_bayes.predict_proba(vectorize_review(review_text))[0,1]
