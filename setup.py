from distutils.core import setup

setup(
    name="django-latency",
    version="0.0.1",
    author="Kevin Mooney",
    author_email="kmooney@gmail.com",
    packages=['latency'],
    scripts=[],
    url='http://pypi.python.org/pypi/django-latency/',
    license='LICENSE.txt',
    description='Destroy the performance of your site (for testing reasons!) with django-latency!',
    long_description=open('README.rst').read(),
    install_requires=[]
)
