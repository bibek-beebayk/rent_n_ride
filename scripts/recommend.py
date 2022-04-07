
from sqlite3 import Error
import csv
import pandas as pd
# import seaborn as sns
import numpy as np
# import sklearn
from sklearn.decomposition import TruncatedSVD
from .csv_generator import generate_csv
# import matplotlib.pyplot as plt
# from surprise import  Reader, Dataset, KNNBasic, KNNWithMeans
# import surprise
# from surprise.model_selection import cross_validate, train_test_split
# from skopt.utils import use_named_args


# print(df)
# print(df.info())
# print(df.describe())

# plt.figure(figsize=(10,6))
# sns.countplot(x='Rating', data=df)
# plt.xlabel('Rating', fontsize=12)
# plt.ylabel('Total Users', fontsize=12)
# plt.show()
# print(df.shape)

def popular_ads():
    generate_csv()

    df = pd.read_csv('ratings.csv')
    popular_ads = pd.DataFrame(df.groupby('ad_id')['review_rating'].count()).sort_values('review_rating', ascending=False)
    # ad_ids = popular_ads['ad_id']
    ad_ids = df['ad_id']
    print(popular_ads)
    print(type(ad_ids))

def recommend_ads(aid): 

    generate_csv()

    df = pd.read_csv('ratings.csv')

    # II
    rating_utility_matrix = df.pivot_table(values='review_rating', index='user_id', columns='ad_id', fill_value=0)
    # print(rating_utility_matrix.shape)

    # Transposing the Matrix
    rating_utility_matrix_transpose = rating_utility_matrix.T
    # print(rating_utility_matrix_transpose.shape)

    # Unique products in subset of data
    unique_products = rating_utility_matrix_transpose

    # Decomposing the matrix
    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(unique_products)
    # print(decomposed_matrix)

    # Correlation Matrix
    correlation_matrix = np.corrcoef(decomposed_matrix)
    # print(correlation_matrix.shape)

    # Isolating specific ad from the correlation_matrix
    user = rating_utility_matrix_transpose.index[9]
    # print(user)

    # index of ad rated by user
    i = aid
    ad_names = list(rating_utility_matrix_transpose.index)
    ad_id = ad_names.index(i)
    # print(ad_id)

    # Correlation for all items with the item purchased by this customer based on items rated by other customers people who bought the same product

    correlation_ad_id = correlation_matrix[ad_id]
    print('Correlation ad_id:', correlation_ad_id)

    # print(np.sort(correlation_ad_id)[::-1])

    recommended_ads = list(rating_utility_matrix_transpose.index[correlation_ad_id>=0.5])
    # recommend.remove(ad_id)
    # print(recommend)
    # print(type(recommend))

    return recommended_ads

popular_ads()