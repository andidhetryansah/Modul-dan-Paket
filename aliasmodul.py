import geometri2D as duaD

def main():

    p = 10
    l = 8

    luas = duaD.luasPersegiPanjang(p, l)

    print("Persegi Panjang")
    print("Panjang\t\t: ", p)
    print("Lebar\t\t: ",l)
    print("Luas\t\t: ", luas)


if __name__ == "__main__":
    main()
