import csv


def page_work(input_country):
    updated_country = list(input_country.split(' '))
    for row in range(len(updated_country)):
        if (updated_country[row] == 'and'
                or updated_country[row] == 'o'
                or updated_country[row] == 'of'):
            continue
        else:
            updated_country[row] = updated_country[row].capitalize()
    final_country = " ".join(updated_country)
    with open('raw_data.csv') as newFile:
        data = csv.reader(newFile, delimiter=',')
        for row in data:
            if row[0] == final_country:
                capital = row[1]
                print(capital)
                break

        return 'Invalid Country Spelling Mistake'

