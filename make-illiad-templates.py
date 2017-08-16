# Load the jinja library's namespace into the current module.
import jinja2
import glob, os
# os.chdir(".")

    
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

for file in glob.glob("*.html"):
    # Read the template file using the environment object.
    # This also constructs our Template object.
    template = templateEnv.get_template( file )

    # Specify any input variables to the template as a dictionary.
    templateVars = { "title" : "Test Example",
                     "description" : "A simple inquiry of function." }
    with open(fname, 'w') as rendered-illiad-templates + '/' + file:
        # Finally, process the template to produce our final text.
        outputText = template.render( templateVars )
        f.write(outputText)

        print(outputText)
