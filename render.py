from string import Template
from settings import TEMPLATE_FOLDER


def read_template(template_name):
    return open(TEMPLATE_FOLDER + template_name, "r").read()


def render(template_name, params):
    string_template = Template(read_template(template_name))
    return string_template.substitute(**params)

