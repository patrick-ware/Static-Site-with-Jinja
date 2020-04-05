import glob
import os

#all_html_files = glob.glob("./content/*.html")
#print(all_html_files)

#file_path = "./content/aboutme.html"
#file_name = os.path.basename(file_path)
#print(file_name)
#name_only, extension = os.path.splitext(file_name)
#print(name_only)

#pages_auto=[]
#all_html_files = glob.glob("./content/*.html")
#for page in all_html_files:
#    filename = os.path.basename(page)
#    name_only, extension = os.path.splitext(filename)
#    pages_auto.append({
#        'filename': filename,
#        'output': "./docs/" + filename,
#        'title': name_only.title(),
#        'image_display': '',
#    })

#print(pages_auto)

def read_page(filename):
    content = open(filename).read()
    return content

page_text = read_page("./content/resume.html")


print(page_text[0])
