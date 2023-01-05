


with open("try/merged_data/merge.txt") as file:
    chunk = 'dummy'
    while chunk != '':
        chunk = file.read(int(1e6))

