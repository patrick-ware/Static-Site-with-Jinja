import utils
import sys

print("This is argv:", sys.argv)
command = sys.argv[0]
while command != "build" and command != "new":
    command = input("Please specify 'build' or 'new':")

if command == "build":
    print("Build was specified")
    utils.main()
elif command == "new":
    print("New page was specified")
    title = input("Choose a title for new page:")

# need to add a create an "add page" func to utils

