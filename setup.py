from distutils.core import setup

with open("./requirements.txt") as f:
    requirements = f.readlines()
f.close()

setup(
  name = 'ttranslator',
  packages = ['ttranslator'],
  version = '0.1',
  license='Apache',
  description = 'Multilingual text translation',
  author = 'Srijan Sharma',
  author_email = 'srijan.sharma.1404@gmail.com',
  url = 'https://github.com/srijan14/text-translation',
  download_url = 'https://github.com/srijan14/text-translation/archive/v_0.1.tar.gz',
  keywords = ['TEXT TRANSLATION', 'MACHINE TRANSLATION'],
  install_requires = requirements
)
