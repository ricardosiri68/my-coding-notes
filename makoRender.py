from mako.template import Template
from mako.lookup import TemplateLookup

f = open("rendered_template.xml","w")
mylookup = TemplateLookup(directories=['.'])
mytemplate = Template(filename="templates/base.xml", lookup=mylookup)
f.write(mytemplate.render())