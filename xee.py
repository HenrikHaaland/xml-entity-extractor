def read_xml_file(file_name, entity_id):

    pattern = f"rdf:ID=\"{entity_id}\""
    print(pattern)
    try:
        file = open(file_name)
        for line in file:
            #print(line, end="")

            if pattern in line:
                print(f"id found in line {line}")
                
        file.close()
        
    except FileNotFoundError: 
        print("file not found")

entity_id = input("skriv inn entity id: ")

#read_xml_file("cim.xml")

read_xml_file("cim-id.xml", entity_id)


