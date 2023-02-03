# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.1.8'


setup(
    name='django-short-url',
    version=version,
    keywords='django-short-url',
    description='Django Short URL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/django-xxx/django-short-url',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_short_url'],
    py_modules=[],
    install_requires=['CodeConvert', 'TimeConvert', 'django-admin>=1.2.4', 'django-models-ext>=1.1.10', 'django-six', 'furl', 'shortuuid'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
