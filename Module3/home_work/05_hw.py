# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_lenght=0
max_lenght_name=''

for name in names:
    if len(name)>max_lenght:
        max_lenght=len(name)
        max_lenght_name=name
print(max_lenght_name)
# TODO: your code here
