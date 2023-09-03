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

# Get user input for the maximum number of workers for "main1"
try:
    max_workers_main1 = int(input("Enter the maximum number of workers for main1: "))
    if max_workers_main1 < 1:
        print("Maximum number of workers for main1 must be at least 1.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter a valid number for the maximum workers for main1.")
    exit(1)

# Calculate the maximum number of workers for "main2" based on the specified factor (3 times)
max_workers_main2 = max_workers_main1 * 3

# Extract the original XML file name (without extension)
original_file_name = os.path.splitext(os.path.basename(xml_file_path))[0]

# Initialize the worker count for "main1" to 1
workers_main1 = 1

# Iterate through worker counts for "main1"
while workers_main1 <= max_workers_main1:
    # Calculate the corresponding worker count for "main2" (3 times "main1")
    workers_main2 = workers_main1 * 3
    
    # Create a deep copy of the root element for each iteration
    new_root = copy.deepcopy(root)
    
    # Find and update the number of workers in main1
    for work in new_root.findall(".//work[@name='main1']"):
        work.set('workers', str(workers_main1))
    
    # Find and update the number of workers in main2
    for work in new_root.findall(".//work[@name='main2']"):
        work.set('workers', str(workers_main2))
    
    # Generate a new XML file name based on the specified format
    updated_file_name = f"{original_file_name}-p{workers_main1}-g{workers_main2}.xml"
    updated_file_path = os.path.join(os.path.dirname(xml_file_path), updated_file_name)
    
    # Save the updated XML to a new file
    tree_copy = ET.ElementTree(new_root)
    tree_copy.write(updated_file_path)
    
    print(f"XML configuration updated for main1={bcolors.YELLOW}{workers_main1}{bcolors.END} and main2={bcolors.YELLOW}{workers_main2}{bcolors.END} workers and saved to {updated_file_name}.")
    
    # Double the worker count for "main1" for the next iteration
    workers_main1 *= 2

print("All configurations have been generated.")
