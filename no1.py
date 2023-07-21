def a000124(n):
    sequence = [1]
    for i in range(1, n):
        sequence.append(sequence[-1] + i)
    return sequence

def main():
    try:
        n = int(input("Masukkan jumlah angka dalam sequence: "))
        if n <= 0:
            print("Masukkan angka yang lebih besar dari 0.")
        else:
            result = a000124(n)
            print("Output:", "-".join(map(str, result)))
    except ValueError:
        print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
