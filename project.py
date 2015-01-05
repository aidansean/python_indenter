from project_module import project_object, image_object, link_object, challenge_object

p = project_object('python_indenter', 'python indenter')
p.domain = 'http://www.aidansean.com/'
p.path = ''
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.github_repo_name = 'python_indenter'
p.mathjax = True
p.links.append(link_object(p.domain, 'pixeler', 'Live page'))
p.introduction = 'This project was made rather quickly to allow the user to quickly indent large python files.'
p.overview = '''The user specifies the input file, output file, start and end lines, type of indentation, and number of characters to indent.  The script fills in missing details if necessary (eg indenting to the end of the file if no end is specified.)'''
