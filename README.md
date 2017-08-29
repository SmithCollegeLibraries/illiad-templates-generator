# Generate templates for ILLiad system

Quick script to run jinja2 templating engine on a set of in-house created templates to create ILLiad system specific templates from smith.edu/libraries front end template.

Things:

1.  Illiad templates (what we want in the end) -- rendered-illiad-templates/
2.  Smith.edu/libraries template code supplied by the primacy (in html/css/js) -- https://github.com/SmithCollegeLibraries/primacy-utility-template
4.  Stock Illiad templates downloaded from the vendor (for reference) -- ILLiad_8.7.0.0_DefaultWebPages/
3.  Autogenerated jinja2 templates created by make-jinja-templates.py based on the Smith.edu/libraries template code and the stock Illiad template files -- autojinjafied-illiad-templates/
4.  Custom jinja2 templates which are hand edited for content changes etc. -- jinjafied-illiad-templates/

## To run
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 make-illiad-templates.py
```

## First time or upgrade from Atlas
```
python3 make-jinja-templates.py
cp autojinjafied-illiad-templates/* jinjafied-illiad-templates/ # or do diff/patch
hack ... hack ... in jinjafied-illiad-templates/
python3 make-illiad-templates.py
```
