import sys

def read_xml_file(file_name, entity_id):

    id_pattern = f"rdf:ID=\"{entity_id}\""

    about_pattern = f"rdf:about=\"{entity_id}\""
    
    print(id_pattern)
    print(about_pattern)
    try:
        with open(file_name) as file:
            line_number = 1
            found_entity = False
            end_tag = ""

            for line in file:
                # print(line, end="")

                if id_pattern in line or about_pattern in line:
                    print(f"id found in line {line_number} {line}")
                    found_entity = True
                    tag = line.split()[0]
                    end_tag = tag[1:]
                    end_tag = f"</{end_tag}>"
                    # print(f"Extracted tag: {tag} {end_tag}")
                    

                if found_entity:
                    print(line, end="")

                if end_tag in line and end_tag !="":
                    found_entity = False
                    # print("fant slutt tag")
                line_number = line_number + 1   

            print(f"totalt antal linjer {line_number}")

    except FileNotFoundError: 
        print("file not found")
print(sys.argv)
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <filename> <entity_id>")
    else:
        file_name = sys.argv[1]
        entity_id = sys.argv[2]
        read_xml_file(file_name, entity_id)



"""
entity_id = input("skriv inn entity id: ")

read_xml_file("cim-id.xml", entity_id)

read_xml_file("cim.xml", entity_id)
"""

