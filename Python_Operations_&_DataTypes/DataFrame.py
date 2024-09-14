import pandas as pd 

data = {
    'name' : ['Ramya', 'Gaythri', 'Rishitha'],
    'age' : [22, 20, 21],
    'city': ['New York', 'LA','Chicago']
}

df = pd.DataFrame(data)
print(df)

#accessing highest aged person name
highest_age_name = df.loc[df['age'].idxmax(), 'name']
print(f'The name of maximum age person is : {highest_age_name}')

#access the city of 'Rishitha'
Rishitha_city = df.loc[df['name'] == 'Rishitha', 'city'].values[0]
print(f'city of Rishitha is : {Rishitha_city}')
