from setuptools import setup, find_packages

setup(
    name='restdemo',
    version='0.1',
    description='demo based on django',
    author='the5fire',
    author_email='123123@163.com',
    url='https://the5fire.com',
    license='MIT',
    packages=find_packages('restdemo'),
    package_dir={'': 'restdemo'},
    package_data={},
    # include_package_data
    install_requires=[
        'django==2.2.22',
        'djangorestframework==3.11.0',
        'coreapi==2.3.3'
    ],
    extras_require={},
    scripts=['restdemo/manage.py'],
    entry_points={
        'console_scripts': ['restdemo_manage=manage:main']
    },
    classifier=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ]
)
