# Generate countries whose names start with a certain letter and print capital of them.

import capital-rd

country = str(input(f'Enter country name: '))

with open('country-list.csv', 'r') as f:
    reader = csv.reader(f)
    items = list(reader)

print(capital-rd.checkCountry(items, country))
