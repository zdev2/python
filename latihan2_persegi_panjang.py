panjang = float(input("masukan panjang : "))
lebar = float(input("masukan lebar   : "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas : {luas} m2, Keliling : {keliling} m")

"""
Trace Table (Contoh Input: panjang = 8, lebar = 5):
+---------+-----------------------------------+---------+-------+------+----------+-----------------------------------+
| Langkah | Baris Kode                        | panjang | lebar | luas | keliling | Output                            |
+---------+-----------------------------------+---------+-------+------+----------+-----------------------------------+
| 1       | panjang = float(input(...))       | 8.0     | -     | -    | -        | masukan panjang : 8               |
| 2       | lebar = float(input(...))         | 8.0     | 5.0   | -    | -        | masukan lebar   : 5               |
| 3       | luas = panjang * lebar            | 8.0     | 5.0   | 40.0 | -        | -                                 |
| 4       | keliling = 2 * (panjang + lebar)  | 8.0     | 5.0   | 40.0 | 26.0     | -                                 |
| 5       | print(...)                        | 8.0     | 5.0   | 40.0 | 26.0     | Luas : 40.0 m2, Keliling : 26.0 m |
+---------+-----------------------------------+---------+-------+------+----------+-----------------------------------+
"""