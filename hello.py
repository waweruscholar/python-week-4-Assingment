# Open the input file in read mode
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# Modify the lines (e.g., convert to uppercase)
modified_lines = [line.upper() for line in lines]

# Open the output file in write mode and write modified lines
with open('output.txt', 'w') as outfile:
    outfile.writelines(modified_lines)

print("File has been modified and saved as 'output.txt'")
