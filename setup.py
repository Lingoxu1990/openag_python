from setuptools import setup, find_packages

setup(
    name='openag',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'couchdb>=1.0.1',
        'requests>=2.10.0',
        'voluptuous>=0.8.11',
        'platformio>=2.11.2'
    ],
    extras_require={
        "test": [
            'mock>=2.0.0',
            'httpretty>=0.8.14',
            'nose>=1.3.7',
            'coverage>=4.2'
        ]
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'openag=openag.cli:main'
        ]
    }
)
