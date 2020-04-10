import utils


def main():
    print("Building site...")
    utils.read_template()
    for page in utils.pages:
        utils.read_page(page)
        utils.insert_content(page)
        utils.write_data(page)
    print("Site built")


if __name__ == "__main__":
    main()
