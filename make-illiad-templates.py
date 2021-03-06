# Load the jinja library's namespace into the current module.
import jinja2
import glob, os
import logging
import argparse

logging.basicConfig(level=logging.INFO)

argparser = argparse.ArgumentParser()
argparser.add_argument("inputPath", help="URL to xml output")
argparser.add_argument("outputPath", help="URL to xml output")

args = argparser.parse_args()

# In this case, we will load templates off the filesystem.
# This means we must construct a FileSystemLoader object.
# 
# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
templateLoader = jinja2.FileSystemLoader( searchpath="." )

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = jinja2.Environment( loader=templateLoader )

for inputFile in glob.glob(args.inputPath + '/' + "*.html"):
    logging.info('Parsing %s' % inputFile)
    inputFileBasename = os.path.basename( inputFile )
    templateName = inputFileBasename.replace('.html', '')
    # Read the template file using the environment object.
    # This also constructs our Template object.
    template = templateEnv.get_template( inputFile )

    # Specify any input variables to the template as a dictionary.
    templateVars = { "templateFilename" : inputFileBasename,  "templateName" : templateName}
    outputFilePath = args.outputPath + '/' + inputFileBasename

    with open(outputFilePath, 'w') as f:
        # Finally, process the template to produce our final text.
        outputText = template.render( templateVars )
        logging.info('Writing %s' % outputFilePath)
        f.write(outputText)
