import pandas as pd

unames = ['user_id','gender', 'age','occupation','zip']
users = pd.read_table('../data/movielens/users.dat',sep='::', header=None, names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../data/movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../data/movielens/movies.dat', sep='::', header=None, names=mnames)

data = pd.merge(pd.merge(ratings,users),movies)
mean_ratings = pd.pivot_table(data,values='rating', index='title',columns='gender', aggfunc='mean')

ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_ratings = mean_ratings.ix[active_titles]
top_female_ratings = mean_ratings.sort_index(by='F', ascending = False)
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
rating_std_by_title = data.groupby('title')['rating'].std()

print(rating_std_by_title.order(ascending=False)[:10])


