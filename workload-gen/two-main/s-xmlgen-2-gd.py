import xml.etree.ElementTree as ET

class bcolors:
    YELLOW = '\033[1;33m'
    END = '\033[0m'

def generate_xml(xml_file, max_worker_count):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    main_workstage = root.find(".//workstage[@name='main']")
    main1_session = main_workstage.find("./work[@name='main1']")
    main2_session = main_workstage.find("./work[@name='main2']")

    worker_count = 2
    while worker_count <= max_worker_count - 1:
        main1_session.set("workers", str(worker_count))
        main2_session.set("workers", str(worker_count))

        modified_xml_file = xml_file.replace('.xml', f'-p{worker_count}-g{worker_count}.xml')
        tree.write(modified_xml_file, encoding='utf-8', xml_declaration='<?xml version="1.0" encoding="UTF-8" ?>')

        worker_count *= 2

    main1_session.set("workers", str(max_worker_count - 1))
    main2_session.set("workers", str(max_worker_count - 1))

    modified_xml_file = xml_file.replace('.xml', f'-g{max_worker_count - 1}-d{max_worker_count - 1}.xml')
    tree.write(modified_xml_file, encoding='utf-8', xml_declaration='<?xml version="1.0" encoding="UTF-8" ?>')

if __name__ == "__main__":
    xml_file_name = input("Enter the XML file name: ")
    max_worker_count = int(input("Enter the maximum number of workers: "))

    generate_xml(xml_file_name, max_worker_count)
    print(f"{bcolors.YELLOW}Modified XML files generated{bcolors.END}")
