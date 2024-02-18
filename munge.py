# place your code to clean up the data file below.
import csv
import os
import pandas as pd
import requests
import json

def get_data():

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    url = "https://data.cityofnewyork.us/resource/s52a-8aq6.json"

    offset = 0
    limit = 1000
    all_data = []

    while True:
        params = {
            "$offset": offset,
            "$limit": limit
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        # Check if data is empty
        if len(data) == 0:
            break

        # Append the current page's data to the overall data list
        all_data.extend(data)

        # Update the offset for the next page
        offset += limit

    platform_agnostic_file_path = os.path.join('data', 'data.json')
    with open(platform_agnostic_file_path, 'w') as file:
        json.dump(all_data, file)

# get_data()

def munge():
    df = pd.read_json('data/data.json')

    df = df.drop(df.columns[-1], axis=1)
    # df = df.drop(['female_2','male_2','grade_k', 'grade_1', 'grade_2',
    #    'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8',
    #    'grade_9', 'grade_10', 'grade_11', 'grade_12', 'asian_2','black_2','hispanic_2', 'multiple_race_categories_not_represented_2',
    #               'white_2','students_with_disabilities_2', 'english_language_learners_2',  'poverty_2'    ], axis=1)


    # check 5

    counts  = df['dbn'].value_counts()
    _p = counts[counts < 5].to_dict()

    for k, v in _p.items():
        index = df[df['dbn'] == k].index[0]
        for i in range(5 - v):
            new_row = df.loc[index].copy()
            new_row.iloc[2:] = 0
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)


    assert not any(df['dbn'].value_counts() < 5)


    platform_agnostic_file_path = os.path.join('data', 'clean_data.csv')
    df.to_csv(platform_agnostic_file_path, index=False)



munge()



