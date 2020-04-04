def main():
	print("Building site...")
	for page in pages:
		insert_header(page)
		insert_content(page)
		write_data(page)
	print("Site built")

#Conditional statement used to insert title and add active page marker to appropriate pages
def insert_header(webpage):
	title = webpage['title']
	template = open('./templates/base.html').read()	

	if title == 'Patrick Ware':
		custom_template = template.replace('{{title}}', webpage['title'])
	else:
		custom_template = template.replace(webpage['title'], '>>'+webpage['title']).replace('{{title}}', webpage['title'])

	return custom_template

#Conditional statement used to correctly place content and modify pageground image based on image_display_value
def insert_content(webpage):
	filename = webpage['filename']
	image_display = webpage['image_display']
	custom_template = insert_header(webpage)
	content = open(filename).read()

	if image_display == 'half':
		combined_page = custom_template.replace('{{view}}', '50%').replace('{{content_halfpage}}', content).replace('{{content_fullpage}}','')
	else:
		combined_page = custom_template.replace('{{view}}', '100%').replace('{{content_fullpage}}', content).replace('{{content_halfpage}}','')
	
	return combined_page

#Combined_page value data passed to write_data function to write file to disk
def write_data(webpage):
	output = webpage['output']
	combined_page = insert_content(webpage)
	open(output, 'w+').write(combined_page)

pages = [	
	{
		'filename': './content/index.html',
		'output': './docs/index.html',
		'title': 'Patrick Ware',
		'image_display': 'full'
	},
	{
		'filename': './content/aboutme.html',
		'output': './docs/aboutme.html',
		'title': 'About Me',
		'image_display': 'half'
	},
	{
		'filename': './content/resume.html',
		'output': './docs/resume.html',
		'title': 'Resume',
		'image_display': 'half'
	},
	{
		'filename':'./content/contact.html',
		'output': './docs/contact.html',
		'title':'Contact',
		'image_display': 'full'
	}
]
	
if __name__ == "__main__":
	main()


