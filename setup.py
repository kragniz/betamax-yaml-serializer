import setuptools

setuptools.setup(
    name='betamax-yaml-serializer',
    version='0.1.0',
    url='https://github.com/kragniz/betamax-yaml-serializer',

    author='Louis Taylor',
    author_email='louis@kragniz.eu',

    description='YAML serializer for betamax',
    long_description=open('README.rst').read(),

    py_modules=['betamax_yaml_serializer'],

    install_requires=[
        'betamax',
        'PyYAML',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
