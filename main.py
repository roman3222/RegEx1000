import re
import csv

with open("phonebook.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_list = []


def names_filter():
    pattern = r'([А-Я])'
    name_substitution = r' \1'
    for cont in contacts_list[1:]:
        sol = cont[0] + cont[1] + cont[2]
        if len((re.sub(pattern, name_substitution, sol).split())) == 3:
            cont[0] = re.sub(pattern, name_substitution, sol).split()[0]
            cont[1] = re.sub(pattern, name_substitution, sol).split()[1]
            cont[2] = re.sub(pattern, name_substitution, sol).split()[2]
        elif len((re.sub(pattern, name_substitution, sol).split())) == 2:
            cont[0] = re.sub(pattern, name_substitution, sol).split()[0]
            cont[1] = re.sub(pattern, name_substitution, sol).split()[1]
            cont[2] = ''
        elif len((re.sub(pattern, name_substitution, sol).split())) == 1:
            cont[0] = re.sub(pattern, name_substitution, sol).split()[0]
            cont[1] = ''
            cont[2] = ''
    return


def phone_number_filter():
    pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    for cont in contacts_list:
        cont[5] = pattern.sub(phone_substitution, cont[5])
    return


def duplicates_filter():
    for cont in contacts_list[1:]:
        first_name = cont[0]
        last_name = cont[1]
        for contact in contacts_list:
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if cont[2] == '':
                    cont[2] = contact[2]
                if cont[3] == '':
                    cont[3] = contact[3]
                if cont[4] == '':
                    cont[4] = contact[4]
                if cont[5] == '':
                    cont[5] = contact[5]
                if cont[6] == '':
                    cont[6] = contact[6]

    for contact in contacts_list:
        if contact not in new_list:
            new_list.append(contact)
    return new_list







if __name__ == '__main__':
    names_filter()
    phone_number_filter()
    duplicates_filter()

    with open("phonebook_final.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)