# Generate templates for ILLiad system

Quick script to run jinja2 templating engine on a set of in-house created templates to create ILLiad system specific templates from smith.edu/libraries front end template.

Things:

1.  Illiad templates (what we want in the end) -- rendered-illiad-templates/
2.  Smith.edu/libraries template code generated by script -- https://github.com/SmithCollegeLibraries/utilitytemplate2.0
4.  Stock Illiad templates downloaded from the vendor (for reference) -- ILLiad_8.7.0.0_DefaultWebPages/
3.  Autogenerated jinja2 templates created by make-jinja-templates.py based on the Smith.edu/libraries template code and the stock Illiad template files -- autojinjafied-illiad-templates/
4.  Custom jinja2 templates which are hand edited for content changes etc. -- jinjafied-illiad-templates/

## To run
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
npm install -g less
bash render.sh
```

## First time or upgrade from Atlas
```
python3 make-jinja-templates.py
cp autojinjafied-illiad-templates/* jinjafied-illiad-templates/ # or do diff/patch
hack ... hack ... in jinjafied-illiad-templates/
python3 make-illiad-templates.py
```

## Less css compiling
render.sh compiles the css automatically

## Deployment
Copy the rendered files to the ftp folder, commit them, and then deploy to the server.
```
# Deploy to staging environment
cp -r rendered-illiad-templates/* ../illiad-folder/
cd ../illiad-folder/
(commit changes)
git ftp push -s testweb
# Check results here: https://smithcollege.illiad.oclc.org/illiad/testweb/illiad.dll
# Must log in here first: https://smithcollege.illiad.oclc.org/illiad/ra-login/illiad.dll

# Deploy to production environment
cp -r rendered-illiad-templates/* ../illiad-folder/
cd ../illiad-folder/
(commit changes)
git ftp push -s prod

```

## Updating make-jinja-templates.py

Because jinjafied-illiad-templates is a hand edited folder we don't want to wipe those changes out with the auto-generated templates. Making a programmatic change to jinja templates requires regenerating the templates then creating a diff and then applying that diff to the jinjafied-illiad-templates folder.

```
edit make-jinja-templates.py
git commit -a -m "Change to jinja template generation code"
python3 make-jinja-templates.py
git diff > mydiff
patch -p2 -d jinjafied-illiad-templates/ < mydiff
# resolve any rejections
```
