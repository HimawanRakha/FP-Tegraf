## Soal 1

> Knight's Tour (Perjalanan Kuda).
> Masalah ini meminta kita untuk menemukan urutan langkah kuda catur pada papan 8 X 8 sedemikian rupa sehingga kuda mengunjungi setiap kotak tepat satu kali.

**Answer:**

- Screenshot

Hasil Visualisasi

<img width="532" height="551" alt="Image" src="https://github.com/user-attachments/assets/24cce699-07a8-4e71-9a44-fa16c3582dc0" />

- Explanation

Menginisiasi Papan catur & gerakan kuda ( x, y )

```
 def __init__(self, size=8):
        self.n = size

        self.board = [[-1 for _ in range(size)] for _ in range(size)]

        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
```

Mengecek apakah langkah berada di dalam papan dan belum dikunjungi

```
 def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.board[y][x] == -1
```

Menghitung berapa banyak langkah valid berikutnya dari posisi (x, y)

```
def get_degree(self, x, y):
        count = 0
        for dx, dy in self.moves:
            if self.is_valid(x + dx, y + dy):
                count += 1
        return count
```

Fungsi untuk mencari solusi dengan

1. Membuat langkah pertama
2. Loop untuk mencari 63 langkah berikutnya
3. Warnsdorff's heuristic dengan memilih langkah yang memiliki tetangga valid paling sedikit
4. Pilih langkah terbaik

```
 def solve(self, start_x, start_y):
```

Fungsi untuk membuat plot visualisasi langkah

```
def visualize(self, path):
```

Inisiasi posisis awal knight dan jalankan fungsi utama

```
start_x = 0
start_y = 0

tour = KnightsTour(8)
success, path = tour.solve(start_x, start_y)

if success:
    print(f"Solusi ditemukan! Total langkah adalah {len(path)}")
    tour.visualize(path)
else:
    print("Solusi tidak ditemukan dengan titik awal tersebut.")
```

<br>

## Soal 2
