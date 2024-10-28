import sys

def logg(message):
    print(message, file=sys.stderr)

def read_xml_file(file_name, entity_id):
    logg(f"searching for {entity_id} in {file_name}")
    id_pattern = f"rdf:ID=\"{entity_id}\""

    about_pattern = f"rdf:about=\"{entity_id}\""
    
    logg(id_pattern)
    logg(about_pattern)
    try:
        with open(file_name) as file:
            line_number = 1
            found_entity = False
            end_tag = ""

            for line in file:
                if id_pattern in line or about_pattern in line:
                    logg(f"id found in line {line_number} {line}")
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

            logg(f"totalt antal linjer {line_number}")

    except FileNotFoundError: 
        logg(f"file not found: {file_name}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        logg("Usage: python xee.py <filename> <entity_id>")
    else:
        file_name = sys.argv[1]
        entity_id = sys.argv[2]
        read_xml_file(file_name, entity_id)