from os import rename, listdir

file_names = listdir('.')
print(file_names)

changed_names = [name.lower().replace(" ", "_") for name in file_names]

for i in range(len(changed_names)):
    rename(file_names[i], changed_names[i])

