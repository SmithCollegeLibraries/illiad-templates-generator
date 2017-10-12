python3 make-illiad-templates.py jinjafied-illiad-templates rendered-illiad-templates
python3 make-illiad-templates.py jinjafied-illiad-templates-ra-login rendered-illiad-templates/ra-login
lessc css/main.less rendered-illiad-templates/css/main.css
lessc css/custom.less rendered-illiad-templates/css/custom.css
lessc css/mobile.less rendered-illiad-templates/css/mobile.css
cp -r rendered-illiad-templates/css rendered-illiad-templates/ra-login/
