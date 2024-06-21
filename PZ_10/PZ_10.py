#В N колхозах выращивают некоторые сельскохозяйственные культуры из имеющегося
#перечня. Определить культуры, выращиваемые во всех колхозах, и культуры,
#выращиваемые только в некоторых из них.
N = int(input("Введите количество колхозов: "))
cultures_all = set()
cultures_some = set()

for i in range(N):
    k = int(input(f"Введите количество культур, выращиваемых в {i + 1}-м колхозе: "))
    cultures = []

    for j in range(k):
        culture = input(f"Введите название {j + 1}-й культуры: ")
        cultures.append(culture)

    if i == 0:
        cultures_all = set(cultures)
    else:
        cultures_all = cultures_all.intersection(cultures)

    cultures_some.update(cultures)

cultures_some -= cultures_all

print("Культуры, выращиваемые во всех колхозах:", ", ".join(cultures_all))
print("Культуры, выращиваемые только в некоторых колхозах:", ", ".join(cultures_some))