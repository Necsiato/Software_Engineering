def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            gen = file.read()
            if not gen:
                raise ValueError("The file is empty")
            print(gen)
    except ValueError as ex:
        print(ex)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    print("Reading from a filled file:")
    read_file("notemptyspace")

    print("Reading from a empty file:")
    read_file("emptyspace.txt")