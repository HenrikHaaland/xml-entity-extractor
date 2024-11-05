import sys
from colorama import init, Fore, Style
init(autoreset=True)

debug = False

def logg(message):
    if debug:
            
        print(message, file=sys.stderr)
    

def read_xml_file(file_name, entity_id):
    logg(f"searching for {entity_id} in {file_name}")
    id_pattern = f"rdf:ID=\"{entity_id}\""
    entity_start_pattern = f"rdf:ID=\""
    about_pattern = f"rdf:about=\"{entity_id}\""
    resource_pattern = f"rdf:resource=\"#{entity_id}\""


    logg(id_pattern)
    logg(about_pattern)
    try:
        with open(file_name) as xml:
            line_number = 1
            found_entity = False
            end_tag = ""
            current_entity = []

            for line in xml:
                if entity_start_pattern in line:
                    found_entity = True
                    tag = line.split()[0]
                    end_tag = tag[1:]
                    end_tag = f"</{end_tag}>"

            
                    
                if found_entity:
                    current_entity.append(line)

                if end_tag in line and end_tag !="":
                    found_entity = False
                    found_id = False
                    for entity_line in current_entity:
                        if id_pattern in entity_line or about_pattern in entity_line or resource_pattern in entity_line:
                            found_id = True
                    if found_id:
                        for entity_line in current_entity:
                            entity_line = entity_line.replace(entity_id, f"{Fore.GREEN}{entity_id}{Style.RESET_ALL}")
                            print(entity_line, end="")

                    current_entity = []
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