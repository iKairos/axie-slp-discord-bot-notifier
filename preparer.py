import os 

required_directories = [
    "assets",
    "assets/images",
    "assets/images/graphs",
    "assets/images/graphs/slp",
    "assets/images/graphs/axs",
]

print("Running preliminary preparations for SLP Bot...")

print("Checking directories...\n")
# Create directories if not exist
for directory in required_directories:
    if os.path.exists(directory):
        print(f"Requirement satisfied: directory {directory} exists.")
    else:
        os.mkdir(directory)
        print(f"Requirement created: directory {directory} does not exist and is created.")

print("\nDirectory checks done.\n")

print("Checking file requirements...\n")

required_files = [
    "secrets.py"
]

for file in required_files:
    if os.path.isfile(file):
        print(f"Requirement satisfied: file {file} exists.")
    else:
        f = open(file, "w+")
        f.write("TOKEN = \" \" # put your bot token here")
        f.close()
        print(f"Requirement created: directory {file} does not exist and is created.")

print("\nFile checks done.\n")

print("You are all set! SLP Bot is good to go!")