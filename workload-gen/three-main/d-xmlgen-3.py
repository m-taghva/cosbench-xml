import xml.etree.ElementTree as ET
import copy
import os

class bcolors:
    YELLOW = '\033[1;33m'
    END = '\033[0m'

# Get user input for the XML file path
xml_file_path = input("Enter the path to the XML configuration file: ")

# Parse the XML configuration file
try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
except FileNotFoundError:
    print("File not found. Please provide a valid XML file path.")
    exit(1)
except ET.ParseError:
    print("Invalid XML file. Please provide a valid XML file.")
    exit(1)

# Get user input for the maximum number
try:
    max_workers = int(input("Enter the maximum number of workers: "))
    if max_workers < 1:
        print("Maximum number of workers must be at least 1.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter a valid number for the maximum workers.")
    exit(1)

# Extract the original XML file name (without extension)
original_file_name = os.path.splitext(os.path.basename(xml_file_path))[0]

# Define the three scenarios
scenarios = [
    {"main1_range": True, "main2_range": False, "main3_range": False},
    {"main1_range": False, "main2_range": True, "main3_range": False},
    {"main1_range": False, "main2_range": False, "main3_range": True}
]

# Function to generate a list of numbers counting in doubles up to max_value
def generate_doubles(max_value):
    num = 1
    doubles = [1]
    while num < max_value:
        num *= 2
        if num <= max_value:
            doubles.append(num)
    return doubles

for i, scenario in enumerate(scenarios, start=1):
    main1_range = scenario["main1_range"]
    main2_range = scenario["main2_range"]
    main3_range = scenario["main3_range"]

    # Generate a list of worker values counting in doubles
    worker_values = generate_doubles(max_workers)

    for workers in worker_values:
        # Create a deep copy of the root element for each iteration
        new_root = copy.deepcopy(root)

        # Find and update the number of workers in main1
        for work in new_root.findall(".//work[@name='main1']"):
            if main1_range:
                work.set('workers', str(workers))
            else:
                work.set('workers', '1')

        # Find and update the number of workers in main2
        for work in new_root.findall(".//work[@name='main2']"):
            if main2_range:
                work.set('workers', str(workers))
            else:
                work.set('workers', '1')

        # Find and update the number of workers in main3
        for work in new_root.findall(".//work[@name='main3']"):
            if main3_range:
                work.set('workers', str(workers))
            else:
                work.set('workers', '1')

        # Generate a new XML file name based on the specified format
        if i == 1:
            updated_file_name = f"{original_file_name}-type{i}-p{workers}-g1-d1.xml"
        elif i == 2:
            updated_file_name = f"{original_file_name}-type{i}-p1-g{workers}-d1.xml"
        elif i == 3:
            updated_file_name = f"{original_file_name}-type{i}-p1-g1-d{workers}.xml"

        updated_file_path = os.path.join(os.path.dirname(xml_file_path), updated_file_name)

        # Save the updated XML to a new file
        tree_copy = ET.ElementTree(new_root)
        tree_copy.write(updated_file_path)

        print(f"Type{bcolors.YELLOW}{i}{bcolors.END}: XML configuration generated {bcolors.YELLOW}{updated_file_name}{bcolors.END}")

print("All configurations have been generated.")
