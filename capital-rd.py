# For the curious minds that already knows where their heart landed.
# Options: categorize countries in alphabetical orders and call for the corrext ones when user prompt Options
# Stack learned countries

import csv

def checkCountry(items, country):
    for item in items:
        if country != item[0]:
            continue
        else:
            return True

def main(items, country):
    while True:
        validCountry = checkCountry(items, country)
        if validCountry == True:
            for item in items:
                if country in item:
                    print(item[1])
                    ans = str(input('Do you want to play again? '))
                    return ans
        else:
            country = str(input(f'Invalid. Please try again: '))


if __name__ == "__main__":
    ans = 'yes'
    while ans.startswith('y'):
        country = str(input(f'Enter country name: '))

        with open('country-list.csv', 'r') as f:
            reader = csv.reader(f)
            items = list(reader)

        ans = main(items, country)
