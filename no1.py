
import matplotlib.pyplot as plt
import numpy as np

class KnightsTour:
    def __init__(self, size=8):
        self.n = size
        # Papan catur diinisialisasi dengan -1 (belum dikunjungi)
        self.board = [[-1 for _ in range(size)] for _ in range(size)]
        # Kemungkinan gerakan kuda (x, y)
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

    def is_valid(self, x, y):
        """Mengecek apakah langkah berada di dalam papan dan belum dikunjungi"""
        return 0 <= x < self.n and 0 <= y < self.n and self.board[y][x] == -1

    def get_degree(self, x, y):
        """Menghitung berapa banyak langkah valid berikutnya dari posisi (x, y)"""
        count = 0
        for dx, dy in self.moves:
            if self.is_valid(x + dx, y + dy):
                count += 1
        return count

    def solve(self, start_x, start_y):
        """Fungsi utama untuk mencari solusi"""
        # Langkah pertama
        self.board[start_y][start_x] = 0
        pos = 1
        curr_x, curr_y = start_x, start_y

        path = [(curr_x, curr_y)]

        # Loop untuk mencari 63 langkah berikutnya
        for i in range(self.n * self.n - 1):
            next_moves = []

            # Cari semua gerakan yang mungkin
            for dx, dy in self.moves:
                nx, ny = curr_x + dx, curr_y + dy
                if self.is_valid(nx, ny):
                    # Warnsdorff's heuristic: Pilih langkah yang memiliki tetangga valid paling sedikit
                    degree = self.get_degree(nx, ny)
                    next_moves.append((degree, nx, ny))

            if not next_moves:
                return False, path # Gagal / Buntu

            # Sortir berdasarkan degree terkecil (Heuristik Warnsdorff)
            next_moves.sort(key=lambda x: x[0])

            # Pilih langkah terbaik
            _, best_x, best_y = next_moves[0]

            self.board[best_y][best_x] = pos
            curr_x, curr_y = best_x, best_y
            path.append((curr_x, curr_y))
            pos += 1

        return True, path

    def visualize(self, path):
        """Membuat plot visualisasi langkah"""
        fig, ax = plt.subplots(figsize=(8, 8))

        # Menggambar papan catur
        for x in range(self.n):
            for y in range(self.n):
                if (x + y) % 2 == 0:
                    ax.add_patch(plt.Rectangle((x, y), 1, 1, color='#f0d9b5'))
                else:
                    ax.add_patch(plt.Rectangle((x, y), 1, 1, color='#b58863'))

        # Menggambar jalur
        x_coords = [p[0] + 0.5 for p in path]
        y_coords = [p[1] + 0.5 for p in path]

        # Plot garis perjalanan
        ax.plot(x_coords, y_coords, color='black', linewidth=1.5, marker='o', markersize=4)

        # Tandai Awal (Hijau) dan Akhir (Merah)
        ax.plot(x_coords[0], y_coords[0], marker='o', markersize=10, color='green', label='Start')
        ax.plot(x_coords[-1], y_coords[-1], marker='X', markersize=10, color='red', label='End')

        # Cek apakah Closed Tour (titik akhir bisa menyerang titik awal)
        start_x, start_y = path[0]
        end_x, end_y = path[-1]
        diff_x = abs(start_x - end_x)
        diff_y = abs(start_y - end_y)
        is_closed = (diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1)

        title = "Knight's Tour Visualization (Heuristic)\n"
        title += "Type: CLOSED Tour" if is_closed else "Type: OPEN Tour"

        if is_closed:
            # Gambar garis penutup putus-putus
            ax.plot([x_coords[-1], x_coords[0]], [y_coords[-1], y_coords[0]],
                    color='blue', linestyle='--', label='Closing Move')

        ax.set_xlim(0, self.n)
        ax.set_ylim(0, self.n)
        ax.set_xticks(range(self.n + 1))
        ax.set_yticks(range(self.n + 1))
        ax.set_aspect('equal')
        ax.grid(True, color='black', linewidth=0.5)
        ax.legend(loc='upper right')
        plt.title(title)
        plt.show()

# --- EKSEKUSI PROGRAM ---
# Anda bisa mengubah posisi awal (x, y) di sini (0-7)
start_x = 0
start_y = 0

tour = KnightsTour(8)
success, path = tour.solve(start_x, start_y)

if success:
    print(f"Solusi ditemukan! Total langkah: {len(path)}")
    tour.visualize(path)
else:
    print("Solusi tidak ditemukan dengan titik awal tersebut.")