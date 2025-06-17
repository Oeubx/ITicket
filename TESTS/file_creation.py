import os

filevar = "previously_logged_in_details.txt"

try:
    # Try creating the file (only if it doesn't exist)
    txtfile = open(filevar, "x")
    txtfile.close()
    print("File created.")
except FileExistsError:
    print("File already exists.")

# Now write to the file (always overwrites)
with open(filevar, "w") as file:
    file.write("3\n")
    file.write("1\n")
    file.write("test\n")
    file.write("test1\n")
    file.write("test@gmail.com\n")
    file.write("0\n")

print("Data written to:", os.path.abspath(filevar))

with open(filevar, "r") as file:
    line1, line2, line3, line4, line5, line6 = [line.strip() for line in file]

#print(line5)