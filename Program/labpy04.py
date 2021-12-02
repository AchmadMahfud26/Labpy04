a = ["Nama : Ari","NIM : 1234","Niali Tugas : 70", "Nilai UTS : 65", "Nilai UAS : 80"]
b = ["Nama : Bambang","NIM : 2345","Niali Tugas : 65", "Nilai UTS : 80", "Nilai UAS : 90"]
for i in a:
    print(i)
jawab = "y"
while jawab == "y" :
    if jawab == "t":
        break
    jawab = input ( "Tambah Data (y/t)? " )
    for i in b:
        print(i)
    jawab = input ( "Tambah Data (y/t)? " )
print("""
=============================================================================
| NO |   NAMA   |  NIM  | NILAI TUGAS | NILAI UTS | NILAI UAS | NILAI AKHIR |
=============================================================================
| 1  | ARI      | 1234  |      70     |    65     |    80     |     71      |
| 2  | BAMBANG  | 2345  |      65     |    80     |    90     |     78      |
=============================================================================
""")