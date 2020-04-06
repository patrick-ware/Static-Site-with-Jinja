import glob
import os
from jinja2 import Template

def main():
    print("Building site...")
    for page in pages:
        insert_header(page)
        insert_content(page)
        write_data(page)
    print("Site built")


# Conditional statement used to insert title and
# add active page marker to appropriate pages
def insert_header(webpage):
    title = webpage['title']
    base_html = open('./templates/base.html').read()
    template = Template(base_html)
    custom_template = template.render({
        'title': title,
})
#    if title == 'Patrick Ware':
#        custom_template = template.replace('{{title}}', webpage['title'])
#    else:
#        custom_template = template.replace(webpage['title'], '>>'+webpage['title']).replace('{{title}}', webpage['title'])

    return custom_template


# Read in content pages 
def read_page(webpage):
    content = open(webpage['filename']).read()
    return content


# Conditional statement used to correctly place content and 
# modify pageground image based on image_display_value
def insert_content(webpage):
    filename = webpage['filename']
    image_display = webpage['image_display']
    custom_template = insert_header(webpage)
    content = read_page(webpage)
    print(content[4:12], filename)

    if content[4:12] == 'halfpage':
        combined_page = custom_template.replace('{{view}}', '50%').replace('{{content_halfpage}}', content).replace('{{content_fullpage}}','')
    else:
        combined_page = custom_template.replace('{{view}}', '100%').replace('{{content_fullpage}}', content).replace('{{content_halfpage}}','')
    
    return combined_page


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
        'output': os.path.join(output_dir, name_only + extension),
        'title': name_only,
        'image_display': '',
    })

    
if __name__ == "__main__":
    main()


