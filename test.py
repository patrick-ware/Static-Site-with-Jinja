# import glob
# import os

# all_html_files = glob.glob("./content/*.html")
# print(all_html_files)

# file_path = "./content/aboutme.html"
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)

# pages = []
# all_html_files = glob.glob("./content/*.html")
# for page in all_html_files:
#    rel_path = os.path.relpath(page)
#    file_name = os.path.basename(page)
#    orig_dir = os.path.dirname(page)
#    output_dir = './docs/'
#    name_only, extension = os.path.splitext(file_name)
#    pages.append({
#        'filename': rel_path,
#        'output': os.path.join(output_dir, name_only + extension),
#        'title': name_only,
#        'image_display': '',
#    })


# print(pages)
# print(rel_path)
# print(file_name)
# print(orig_dir)
# print(output_dir)
# print(name_only)
# print(extension)

#def read_page(filename):
#    content = open(filename).read()
#    return content


#page_text = read_page("./content/resume.html")


#print(page_text[0])

from jinja import Template
index_html = open("./content/index.html").read()

template_html = open("templatebase.html").read()
template = Template(templates_html)
template.render(
    title = "Homepage",
    content = index_html,
)
