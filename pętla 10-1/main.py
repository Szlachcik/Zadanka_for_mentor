exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}
print("Failed students:")
for failed_students in exam_points:
    if exam_points[failed_students]<46:
        print(failed_students)
print("Top students:")
for top_students in exam_points:
    if exam_points[top_students]>90:
        print(  top_students)

failed_students = []
top_students = []
best_student = ("",0)

# przykład rozwiązania zadania
lista = [1, 3, 7, 11, 2, -6, 0]
# zmienne przecowujące najmniejsza i największa wartość
# na poczatku przypisujemy im wartość None, aby w pętli for
# wiedzieć że jest to pierwsza interakcja
# później zmienne, zaczynają zawierać liczby z listy
najmniejsza = None
najwieksza = None
for i in lista:

    # przy każdej iteracji, sprawdzamy czy zmienna i
    # jest mniejsza lub większa niż przechowywane przez
    # nas zmienne

    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i

    if najwieksza == None or najwieksza < i:
        najwieksza = i

print("najmniejsza liczba to:", najmniejsza)
print("największa liczba to:", najwieksza)
