import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='keys',
    version='0.1.3',
    author='N/A',
    author_email='joshua.haught@rollinghills.k12.oh.us',
    description='School package for keypress recognition',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jagg3127/lib',
    project_urls = {
        "Bug Tracker": "https://github.com/jagg3127/lib/issues"
    },
    license='MIT',
    packages=['keys'],
    install_requires=['pynput'],
)