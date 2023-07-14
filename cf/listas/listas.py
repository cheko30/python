lista_cursos = ['Python', 'Djnango', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']

sub_lista = lista_cursos[0:3]
print(sub_lista)

print(len(lista_cursos))

lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')

lista_cursos.extend(lista_cursos_2)

print(lista_cursos)
print(lista_cursos_2)

# Metodos
lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
lista.sort()

print(lista[0]) # min
print(lista[-1]) # max

print(min(lista))
print(max(lista))