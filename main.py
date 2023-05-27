from schrage import schrage_algorithm


def main():
    file_input = [tuple(map(int, i.rstrip().split()))
                  for i in open('data/SCHRAGE1.DAT').readlines()[1:]]
    output = schrage_algorithm(file_input)
    cmax, measurement_time = output
    print(f"Cmax = {cmax} in {measurement_time} seconds.")


if __name__ == "__main__":
    main()
