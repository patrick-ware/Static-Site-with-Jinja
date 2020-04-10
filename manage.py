import glob
import os
from jinja2 import Template


def main():
    print("Building site...")
    read_template()
    for page in pages:
        read_page(page)
        insert_content(page)
        write_data(page)
    print("Site built")


if __name__ == "__main__":
    main()
