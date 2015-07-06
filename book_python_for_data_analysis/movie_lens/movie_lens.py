import pandas as pd

unames = ['user_id','gender', 'age','occupation','zip']
users = pd.read_table('../data/movielens/users.dat',sep='::', header=None, names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../data/movielens/ratings.dat', sep='::', header=None, names=rnames)
#print(ratings)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../data/movielens/movies.dat', sep='::', header=None, names=mnames)

data = pd.merge(pd.merge(ratings,users),movies)
mean_ratings = pd.pivot_table(data,values='rating', index='title',columns='gender', aggfunc='mean')

print(mean_ratings[:5])


