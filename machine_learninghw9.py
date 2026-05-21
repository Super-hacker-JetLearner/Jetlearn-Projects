import pandas as pd

# recommender
# simple recommendation


data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/entree+chicago+recommendation+data/entree/data/atlanta.txt', sep='\t',header=None,index_col=0)

print(data)


def get_count(row):
    the_list = row[2].split(' ')
    count = len(the_list)
    return count


data['count'] = data.apply(axis=1,func=get_count)


print(data)


data = data.sort_values('count',ascending=False)

print(data[[1,'count']].head(10))


# simple, content, colaborative