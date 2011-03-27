from paste.script.templates import Template, var
from paste.util.template import paste_script_template_renderer as renderer

vars = [
    var('project_name', 'Name of the project (like "My Project")'),
    var('package_name', 'Name of the project package (like "my_project")'),
    var('description', 'Description of the project'),
    var('version', 'Project Version (like 0.1)', default='0.1'),
    var('django_version', 'Django Version (like 1.3)', default='1.3'),
    var('author', 'Author name'),
    var('author_email', 'Author email'),
]


class DjangoProjectBuildoutTemplate(Template):
    egg_plugins = ['DjangoProjectBuildout']
    summary = 'Template for creating a Django project with zc.buildout'
    # required_templates = []
    _template_dir = 'template'
    vars = vars
    template_renderer = staticmethod(renderer)

    def pre(self, command, output_dir, vars):
        # Generate secret_key
        from random import choice
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = ''.join([choice(chars) for i in range(50)])
        vars['secret_key'] = secret_key

