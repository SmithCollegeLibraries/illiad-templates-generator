# Generate templates for ILLiad system

Quick script to run jinja2 templating engine on a set of in-house created templates to create ILLiad system specific templates from smith.edu/libraries front end template.

Things:

1.  Illiad templates (what we want in the end) -- rendered-illiad-templates/
2.  Smith.edu/libraries template code supplied by the primacy (in html/css/js) -- https://github.com/SmithCollegeLibraries/primacy-utility-template
3.  Custom jinja2 templates which are hand created based on the Smith.edu/libraries template code and the stock Illiad template files -- jinjafied-illiad-templates/
4.  Stock Illiad templates downloaded from the vendor (for reference) -- ILLiad_8.7.0.0_DefaultWebPages/

## To run
```python3 make-illiad-templates.py```
