import utils
import sys
import re

print("This is argv:", sys.argv)
command = sys.argv[-1]
while command.casefold() != "build" and command.casefold() != "new":
    print("--> Rebuild site: python manage.py build")
    print("--> Create new page: python manage.py new")
    command = input("Please specify 'build' or 'new':")

if command.casefold() == "build":
    print("Build was specified")
    utils.main()
elif command.casefold() == "new":
    print("New page was specified")
    title = input("Choose a title for new page:")
    sanitized_title = re.sub('[\W_]+', '_', title)
    utils.new_page(sanitized_title, title)
    print("New page was created")
