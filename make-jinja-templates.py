from bs4 import BeautifulSoup
import glob, os
import logging
from string import Template
import re

logging.basicConfig(level=logging.INFO)

inputPath = 'ILLiad_8.7.0.0_DefaultWebPages'
outputPath = 'autojinjafied-illiad-templates'

top = """
{% extends "layouts/layout.html" %}
{% block title %}$title{% endblock %}

{% block content %}
<!-- Template file: {{ templateFilename }} -->
<div id="wrap">
    <#INCLUDE filename="include_header.html">
    <h1>{{ self.title() }}</h1>
    <div id="content-wrap">
        <#INCLUDE filename="include_menu.html">
        <div class="col-sm-10">
        <div id="status"><#STATUS></div>
          <!-- MAIN CONTENT AREA -->
"""

#import pdb; pdb.set_trace()

bottom = """
          <!-- / MAIN CONTENT AREA -->
        </div>
    </div>
{% endblock %}
"""

for inputFileName in glob.glob(inputPath + '/' + "*.html"):
    logging.info('Processing %s' % inputFileName)
    with open(inputFileName) as fp:
        template = fp.read()
        template = re.sub("name\=\"(.*?)\"", r"""name='\1'""", template, flags=re.DOTALL)
        soup = BeautifulSoup(template, "html5lib")
        contents = soup.select("div#content")
        try:
            content = contents[0]
        except IndexError:
            logging.warning('Could not parse %s' % inputFileName)
            continue
        # Set title
        title = soup.find('title').string
        title = title.replace("ILLiad - ","") 
        topTemplate = Template(top)
        topWithTitle = topTemplate.substitute({'title': title})

        # Remove #content id from the wrapper div
        del content['id']

        # Write full page template
        content_text = content.prettify(formatter=None)
        outputFilePath = outputPath + '/' + os.path.basename( inputFileName )
        logging.info('Writing %s' % outputFilePath)
        with open(outputFilePath, "w") as f:
            f.write(topWithTitle)
            f.write(content_text)
            f.write(bottom)
#        print(content)
