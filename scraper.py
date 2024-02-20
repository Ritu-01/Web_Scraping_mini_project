import requests
from bs4 import BeautifulSoup
import pandas as pd
req = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")

soup = BeautifulSoup(req.text,'html.parser')


#find the table containing the data
table = soup.find('table', class_ ='wikitable sortable')

# Extract column headers
#strip() to clear /n
headers = [header.text.strip() for header in table.find_all('th')]

#Initialize an empty Dataframe with the headers
df = pd.DataFrame (columns = headers)

#Extract data rows from the table
for row in table.find_all('tr')[1:]:
    row_data = [cell.text.strip() for cell in row.find_all('td')]
    # Create a DataFrame row using the row data
    df.loc[len(df)] = row_data

# Display the DataFrame
print(df)
df.to_csv('largest_companies_usa.csv', index= False)
print("Data saved to largest_companies_usa.csv")
