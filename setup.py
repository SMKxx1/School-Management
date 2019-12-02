from setuptools import setup

setup(
    name = "sclmgt",
    version = "1.0.0",
    packages = ['sclmgt'],
    entry_points = {
        'console_scripts': [
            'sclmgt = sclmgt.__main__:main'
        ]
    }
)