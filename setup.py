from setuptools import find_packages, setup, Command
import io
import os
import sys
from shutil import rmtree

NAME = 'text-translator'
DESCRIPTION = 'Multilingual text translation'
URL = 'https://github.com/srijan14/text-translation'
EMAIL = 'srijan.sharma.1404@gmail.com'
AUTHOR = 'Srijan Sharma'
LICENCE = 'Apache'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '1.5'
CONTENT_TYPE = "text/markdown"

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}


if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else :
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()

setup(
  name=NAME,
  packages=find_packages(exclude=("tests",)),
  long_description_content_type=CONTENT_TYPE,
  version =VERSION,
  url=URL,
  license=LICENCE,
  description = DESCRIPTION,
  long_description = long_description,
  author = AUTHOR,
  author_email = EMAIL,
  requires_python = REQUIRES_PYTHON,
  keywords = ['TEXT TRANSLATION', 'MACHINE TRANSLATION'],
  install_requires=['certifi==2019.9.11', 'chardet==3.0.4', 'ConfigArgParse==0.15.1', 'idna==2.8',
                    'numpy==1.17.4', 'requests==2.22.0', 'sentencepiece==0.1.83', 'six==1.13.0',
                    'torch==1.3.1', 'torchtext==0.4.0', 'tqdm==4.38.0', 'urllib3==1.25.7', 'onmt==1.0.0'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',  # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  # Again, pick a license
    'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
