import os

def read_data_from_file():
    try:
        with open("./cities.txt", "r") as f:
            file_lines = []
            count = 1
            try:
                line = f.readline()
                while(line):
                    line = str(count) + ": " + line
                    file_lines.append(line)
                    count += 1
                    line = f.readline()
            except Exception as e:
                print("An error occured while reading the file")
                print(str(e))
                return []
            else:
                return file_lines
    except (OSError, IOError) as e:
        print("An error occured while trying to open the file. Please check again if the file exists")
        return []

def write_data_to_file(file_lines):
    path = "./"
    filename = "out.txt"
    if len(file_lines) == 0:
        print("An empty list was given")
        return
    try:
        with open(os.path.join(path, filename), "w") as f:
            try:
                for line in file_lines:
                    f.write(line)
            except Exception as e:
                print("An error occured while trying to write in the out.txt file. Please try again")
                print(str(e))
    except (OSError, IOError) as e:
        print("An error occured while trying to open the file. Please check again if the file exists")

if __name__ == '__main__':
    file_lines = read_data_from_file()
    write_data_to_file(file_lines)