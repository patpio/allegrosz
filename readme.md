# Allegrosz

c.execute('DROP TABLE IF EXISTS item')  # METODA, co chcemy, warunek, item: nazwy tabel w liczbie pojedynczej, male litery

c.executemany('INSERT INTO category (name) VALUES (?)', categories)  # ilosc pytajnikow po przecinku oznacza ilosc kolumn ktore wypelniamy, tuple wieloelementowe

import - wbudowane, third party, nasze - kolejnosc!!!

CRUD - Create Read Update Delete

RESTAPI - POST, GET, PUT/PATCH, DELETE

SQL - INSERT, SELECT, UPDATE, DELETE

relacje miedzy tabelami: 1:1, 1:wielu, wiele:wielu

item.category  . w jinja wartosc z slownika

koercja - niejawne rzutowanie typow danych