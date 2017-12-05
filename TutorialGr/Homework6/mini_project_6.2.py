def read_binary_file():
    try:
        with open("./imag", "rb") as im:
            file_bytes = []
            try:
                count = 0
                byte = im.read(1)
                while(byte and count<3):
                    file_bytes.append(byte)
                    count +=1
                    byte = im.read(1)
            except Exception as e:
                print("An error occured while reading the file")
                print(str(e))
                return []
            else:
                return file_bytes
    except (OSError, IOError) as e:
        print("An error occured while trying to open the binary file. Please check again if the file exists")
        print(str(e))
        return []

def check_for_jpg(file_bytes):
    if len(file_bytes) == 0:
        print("Empty list was given. Please try again")
        return
    jpg_file = [255, 216, 255]
    dec_values = []
    hex_values = []
    for byte_in_file in file_bytes:
        integer_value = int.from_bytes(byte_in_file, byteorder='big', signed=False)
        hex_value = hex(integer_value)
        print(str(integer_value) + "\t" + str(hex_value))
        dec_values.append(integer_value)
        hex_values.append(hex_value)
    flag = True
    for i,byte in enumerate(dec_values):
        if byte != jpg_file[i]:
            flag = False
    if flag ==True:
        print("The file is of type jpg")
    else:
        print("The file is not of type jpg")

if __name__ == '__main__':
    file_bytes = read_binary_file()
    check_for_jpg(file_bytes)