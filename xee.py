def read_xml_file():
    file_name = "cim.xml"

    try:
        file = open(file_name)
        print(file.read())
        file.close()
    except FileNotFoundError: 
        print("file not found")

read_xml_file()

