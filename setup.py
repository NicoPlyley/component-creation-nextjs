from setuptools import setup

setup(
    name='mkcomponent',
    version='1.0.0',
    packages=['mkcomponent'],
    entry_points={
        'console_scripts': [
            'mkcomponent = mkcomponent.__main__:main'
        ]
    })
