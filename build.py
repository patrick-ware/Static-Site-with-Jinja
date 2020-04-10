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


# Read in template
def read_template():
    base_html = open('./templates/base.html').read()
    return base_html


# Read in content pages and assign 'view' value
def read_page(webpage):
    content = open(webpage['filename']).read()
    webpage['view'] = content[4:8]
    return content


# Insert content and format page
def insert_content(webpage):
    title = webpage['title']
    view = webpage['view']
    base_html = read_template()
    content = read_page(webpage)
    template = Template(base_html)
    custom_template = template.render({
            'title': title,
            'content': content,
            'view': view,
            'pages':pages,
        })

    return custom_template


# Combined_page value data passed to write_data function to write file to disk
def write_data(webpage):
    output = webpage['output']
    combined_page = insert_content(webpage)
    open(output, 'w+').write(combined_page)


pages = []

all_html_files = glob.glob("./content/*.html")

for page in all_html_files:
    rel_path = os.path.relpath(page)
    file_name = os.path.basename(page)
    name_only, extension = os.path.splitext(file_name)
    orig_dir = os.path.dirname(page)
    output_dir = './docs/'
    pages.append({
        'filename': rel_path,
        'url': name_only + extension,
        'output': os.path.join(output_dir, name_only + extension),
        'title': name_only,
        'view': '',
    })


if __name__ == "__main__":
    main()
