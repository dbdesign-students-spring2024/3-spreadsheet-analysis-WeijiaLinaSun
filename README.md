# Report on "2013 - 2018 Demographic Snapshot School"

## Dataset details:

The dataset is called [2013 - 2018 Demographic Snapshot Schools](https://data.cityofnewyork.us/Education/2013-2018-Demographic-Snapshot-School/s52a-8aq6/about_data) and comes from the NYC Open Data website. It provides demographic data for New York City public schools from 2013 through 2018, and the data can be accessed at this link.

## Raw data format:

The raw data file is in JSON format.

## Raw data (first 20 rows):

| DBN    | School Name                    | Year    | Total Enrollment | Grade PK (Half Day & Full Day) | Grade K | Grade 1 | Grade 2 | Grade 3 | Grade 4 | Grade 5 | Grade 6 | Grade 7 | Grade 8 | Grade 9 | Grade 10 | Grade 11 | Grade 12 | # Female | % Female | # Male | % Male | # Asian | % Asian | # Black | % Black | # Hispanic | % Hispanic | # Multiple Race Categories Not Represented | % Multiple Race Categories Not Represented | # White | % White | # Students with Disabilities | % Students with Disabilities | # English Language Learners | % English Language Learners | # Poverty | % Poverty | Economic Need Index |
| ------ | ------------------------------ | ------- | ---------------- | ------------------------------ | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- | -------- | -------- | -------- | -------- | ------ | ------ | ------- | ------- | ------- | ------- | ---------- | ---------- | ------------------------------------------ | ------------------------------------------ | ------- | ------- | ---------------------------- | ---------------------------- | --------------------------- | --------------------------- | --------- | --------- | ------------------- |
| 01M015 | P.S. 015 Roberto Clemente      | 2013-14 | 190              | 26                             | 39      | 39      | 21      | 16      | 26      | 23      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 93       | 48.9     | 97     | 51.1   | 9       | 4.7     | 72      | 37.9    | 104        | 54.7       | 2                                          | 1.1                                        | 3       | 1.6     | 65                           | 34.2                         | 19                          | 10                          | 171       | 90        | No Data             |
| 01M015 | P.S. 015 Roberto Clemente      | 2014-15 | 183              | 18                             | 27      | 47      | 31      | 19      | 17      | 24      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 84       | 45.9     | 99     | 54.1   | 8       | 4.4     | 65      | 35.5    | 107        | 58.5       | 1                                          | 0.5                                        | 2       | 1.1     | 64                           | 35                           | 17                          | 9.3                         | 169       | 92.3      | 93.50%              |
| 01M015 | P.S. 015 Roberto Clemente      | 2015-16 | 176              | 14                             | 32      | 33      | 39      | 23      | 17      | 18      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 83       | 47.2     | 93     | 52.8   | 9       | 5.1     | 57      | 32.4    | 105        | 59.7       | 3                                          | 1.7                                        | 2       | 1.1     | 60                           | 34.1                         | 16                          | 9.1                         | 149       | 84.7      | 89.60%              |
| 01M015 | P.S. 015 Roberto Clemente      | 2016-17 | 178              | 17                             | 28      | 33      | 27      | 31      | 24      | 18      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 83       | 46.6     | 95     | 53.4   | 14      | 7.9     | 51      | 28.7    | 105        | 59         | 4                                          | 2.2                                        | 4       | 2.2     | 51                           | 28.7                         | 12                          | 6.7                         | 152       | 85.4      | 89.20%              |
| 01M015 | P.S. 015 Roberto Clemente      | 2017-18 | 190              | 17                             | 28      | 32      | 33      | 23      | 31      | 26      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 99       | 52.1     | 91     | 47.9   | 20      | 10.5    | 52      | 27.4    | 110        | 57.9       | 2                                          | 1.1                                        | 6       | 3.2     | 45                           | 23.7                         | 8                           | 4.2                         | 161       | 84.7      | 89.00%              |
| 01M019 | P.S. 019 Asher Levy            | 2013-14 | 285              | 36                             | 39      | 38      | 36      | 45      | 47      | 44      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 141      | 49.5     | 144    | 50.5   | 41      | 14.4    | 56      | 19.6    | 148        | 51.9       | 10                                         | 3.5                                        | 30      | 10.5    | 89                           | 31.2                         | 25                          | 8.8                         | 213       | 74.7      | No Data             |
| 01M019 | P.S. 019 Asher Levy            | 2014-15 | 270              | 30                             | 44      | 40      | 39      | 35      | 40      | 42      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 132      | 48.9     | 138    | 51.1   | 30      | 11.1    | 47      | 17.4    | 158        | 58.5       | 8                                          | 3                                          | 27      | 10      | 82                           | 30.4                         | 18                          | 6.7                         | 200       | 74.1      | 60.90%              |
| 01M019 | P.S. 019 Asher Levy            | 2015-16 | 270              | 21                             | 47      | 43      | 41      | 43      | 35      | 40      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 125      | 46.3     | 145    | 53.7   | 27      | 10      | 55      | 20.4    | 169        | 62.6       | 3                                          | 1.1                                        | 16      | 5.9     | 82                           | 30.4                         | 13                          | 4.8                         | 217       | 80.4      | 63.00%              |
| 01M019 | P.S. 019 Asher Levy            | 2016-17 | 271              | 24                             | 37      | 46      | 47      | 40      | 43      | 34      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 127      | 46.9     | 144    | 53.1   | 24      | 8.9     | 51      | 18.8    | 180        | 66.4       | 1                                          | 0.4                                        | 15      | 5.5     | 88                           | 32.5                         | 9                           | 3.3                         | 207       | 76.4      | 58.20%              |
| 01M019 | P.S. 019 Asher Levy            | 2017-18 | 257              | 13                             | 34      | 38      | 42      | 46      | 42      | 42      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 114      | 44.4     | 143    | 55.6   | 23      | 8.9     | 49      | 19.1    | 166        | 64.6       | 3                                          | 1.2                                        | 16      | 6.2     | 87                           | 33.9                         | 8                           | 3.1                         | 197       | 76.7      | 67.20%              |
| 01M020 | P.S. 020 Anna Silver           | 2013-14 | 631              | 54                             | 114     | 111     | 98      | 109     | 71      | 74      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 305      | 48.3     | 326    | 51.7   | 223     | 35.3    | 54      | 8.6     | 314        | 49.8       | 16                                         | 2.5                                        | 24      | 3.8     | 144                          | 22.8                         | 104                         | 16.5                        | 448       | 71        | No Data             |
| 01M020 | P.S. 020 Anna Silver           | 2014-15 | 633              | 51                             | 102     | 108     | 100     | 98      | 104     | 70      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 301      | 47.6     | 332    | 52.4   | 231     | 36.5    | 53      | 8.4     | 309        | 48.8       | 15                                         | 2.4                                        | 25      | 3.9     | 144                          | 22.7                         | 120                         | 19                          | 411       | 64.9      | 72.70%              |
| 01M020 | P.S. 020 Anna Silver           | 2015-16 | 581              | 46                             | 82      | 90      | 98      | 92      | 81      | 92      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 277      | 47.7     | 304    | 52.3   | 204     | 35.1    | 46      | 7.9     | 286        | 49.2       | 21                                         | 3.6                                        | 24      | 4.1     | 123                          | 21.2                         | 88                          | 15.1                        | 353       | 60.8      | 68.30%              |
| 01M020 | P.S. 020 Anna Silver           | 2016-17 | 540              | 41                             | 83      | 83      | 92      | 95      | 77      | 69      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 265      | 49.1     | 275    | 50.9   | 175     | 32.4    | 52      | 9.6     | 264        | 48.9       | 22                                         | 4.1                                        | 27      | 5       | 116                          | 21.5                         | 93                          | 17.2                        | 315       | 58.3      | 68.00%              |
| 01M020 | P.S. 020 Anna Silver           | 2017-18 | 497              | 34                             | 71      | 82      | 69      | 89      | 83      | 69      | 0       | 0       | 0       | 0       | 0        | 0        | 0        | 244      | 49.1     | 253    | 50.9   | 147     | 29.6    | 51      | 10.3    | 264        | 53.1       | 19                                         | 3.8                                        | 16      | 3.2     | 114                          | 22.9                         | 86                          | 17.3                        | 356       | 71.6      | 79.20%              |
| 01M034 | P.S. 034 Franklin D. Roosevelt | 2013-14 | 393              | 18                             | 33      | 32      | 35      | 34      | 45      | 43      | 43      | 57      | 53      | 0       | 0        | 0        | 0        | 196      | 49.9     | 197    | 50.1   | 26      | 6.6     | 108     | 27.5    | 246        | 62.6       | 1                                          | 0.3                                        | 12      | 3.1     | 129                          | 32.8                         | 25                          | 6.4                         | 373       | 94.9      | No Data             |
| 01M034 | P.S. 034 Franklin D. Roosevelt | 2014-15 | 395              | 18                             | 40      | 32      | 29      | 35      | 32      | 44      | 63      | 43      | 59      | 0       | 0        | 0        | 0        | 199      | 50.4     | 196    | 49.6   | 25      | 6.3     | 110     | 27.8    | 245        | 62         | 1                                          | 0.3                                        | 14      | 3.5     | 119                          | 30.1                         | 26                          | 6.6                         | 381       | 96.5      | 86.00%              |
| 01M034 | P.S. 034 Franklin D. Roosevelt | 2015-16 | 394              | 18                             | 33      | 41      | 30      | 27      | 36      | 33      | 64      | 62      | 50      | 0       | 0        | 0        | 0        | 200      | 50.8     | 194    | 49.2   | 18      | 4.6     | 113     | 28.7    | 249        | 63.2       | 0                                          | 0                                          | 14      | 3.6     | 122                          | 31                           | 29                          | 7.4                         | 384       | 97.5      | 86.10%              |
| 01M034 | P.S. 034 Franklin D. Roosevelt | 2016-17 | 350              | 13                             | 21      | 24      | 37      | 31      | 29      | 36      | 38      | 59      | 62      | 0       | 0        | 0        | 0        | 170      | 48.6     | 180    | 51.4   | 19      | 5.4     | 102     | 29.1    | 216        | 61.7       | 2                                          | 0.6                                        | 11      | 3.1     | 130                          | 37.1                         | 27                          | 7.7                         | 348       | 99.4      | 86.80%              |

## Problems with the dataset include:

There are missing values in the dataset, Economic Need Index contains "No Data", which means data is missing, the column was removed using python. 

As well, for the missing years, only the DBN and school name columns are filled in, and the rest of the missing columns are replaced with zeros.

``` python
# Remove the Economic Need Index column information.
df = df.drop(df.columns[-1], axis=1)

# Find the data records that are less than five years old based on the dbn column.
counts = df['dbn'].value_counts()
_p = counts[counts < 5].to_dict()
# Completes the data records one by one based on the data records found earlier.
for k, v in _p.items():.
# Find the row number of the missing record.
	index = df[df['dbn'] == k].index[0]
  for i in range(5 - v).
# Copy the current missing record data.
  	new_row = df.loc[index].copy()
# Replace all missing information with 0 except for the DBN column and the school name column.
  	new_row.iloc[2:] = 0
# Take the newly added rows and splice them to the end of the table.
		df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
# Check again to see if the data is all five years old.
assert not any(df['dbn'].value_counts() < 5)
```

## Data file links:

[the original data file](./data/data.json)

[the munged data file](./data/clean_data.csv)

[the spreadsheet file](./data/analysis.xlsx)

## Description of the computational data:

1. I calculated the maximum values for grade 1 and their corresponding DBNs and school names. This helps to pinpoint the names and DBNs of the schools that had the highest number of students in first grade in New York City public schools from 2013 to 2018. I used the formula "=MATCH(MAX(G:G), G:G, 0)" for locating the row number in Excel that has the maximum number of first-grade students, with the number of first graders being in the G column. MAX (G: G) is part of calculating the maximum value of all cells in column G, that is, all the first-year students in the maximum value. MATCH (MAX (G: G), G: G, 0) part of the search for the maximum value of this relative position in column G (row number). The third parameter of the MATCH function, 0, indicates that the lookup is for an exact match. This formula returns the cell containing the maximum first-year students in the G column of the relative position (row number). This row number is then used with the INDEX function to find the DBN and school name for the same row. Use the formula "= INDEX (A: A, MATCH (MAX (G: G), G: G, 0))" to find the corresponding DBN. Use the formula "= INDEX (B: B, MATCH (MAX (G: G), G: G, 0)) " to find the corresponding school name.
2. I calculated the minimum value for grade 1, and in the same way as the first one, by replacing MAX with MIN in the operation of the first one, I can also find the name and DBN of the school that has the smallest number of first graders.
3. I calculated the total number of people of different races (asian, black, hispanic, white, and multiple race categories not represented) across all schools and all years. I first identified the race column, for example asian as column W. I then used the SUM function to calculate the total. Then I used the SUM function to calculate the total using the formula "=SUM(W:W)" to calculate the total number of asians. Perform this for each race in a new cell.
4. I calculated the average of english language learners for all schools from 2013-2018. I first determined the column of english language learners as AI and then used the AVERAGE function to get the average using the formula "=AVERAGE(AI:AI)" used in Excel.

## Chart Visualization:

I created a pie chart titled "Ethnic demographics". The chart shows ethnic demographics from the 2013-2018 Demographic Snapshot School. The sections of the pie chart represent the percentage of different racial groups in the whole. Specifically:

![Ethnic demographics](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-WeijiaLinaSun/blob/main/images/Ethnic%20demographics.png)

* "Hispanic_sum" is the largest group at 40%.
* "Black_sum" is the second largest at 27%.
* "Asian_sum" is 16%.
* "White_sum" is 15%.
* "Multiple_race_categories_not_represented_sum" is the smallest at 2%.

This pie chart provides a visual representation of the racial distribution, showing that Hispanics make up the largest percentage of the New York City public school population from 2013 to 2018, while multiracial but unspecified groups make up the smallest percentage. The chart shows the relative size of the different races in the dataset and can help one understand the diversity of the school community.

## Extra-credit

This assignment deserves extra points because instead of downloading the data directly from the internet, I crawled the data by means of python crawler and saved it locally in json format. In the process of crawling, due to the data website settings, only a thousand pieces of data can be crawled at a time, so that's why I used multiple crawls until all the data was crawled. 

```python
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
```

In addition, I also chose a large data table (Rows: 8,972, Columns: 39) for processing.