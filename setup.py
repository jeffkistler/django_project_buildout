from setuptools import setup, find_packages
import sys, os

version = '0.1'

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='django_project_buildout',
    version=version,
    description='A Paste Script template for a full Django project skeleton with zc.buildout.',
    long_description=read('README.rst'),
    classifiers=[
        'Framework :: Django',
        'Framework :: Paste',
        'Framework :: Buildout',
        'Intended Audience :: Developers',
    ],
    keywords='paste templates django',
    author='Jeff Kistler',
    author_email='jeff@jeffkistler.com',
    url='https://github.com/jeffkistler/django_project_buildout',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'PasteScript>=1.3'
    ],
    entry_points="""
    [paste.paster_create_template]
    django_project=django_project_buildout.templates:DjangoProjectBuildoutTemplate
    """,
)
