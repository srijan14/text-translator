from distutils.core import setup

with open("./requirements.txt") as f:
    requirements = f.readlines()
f.close()

setup(
  name='ttranslator',
  packages = ['ttranslator'],
  version = '0.1',
  license='Apache',
  description = 'Multilingual text translation',
  author = 'Srijan Sharma',
  author_email = 'srijan.sharma.1404@gmail.com',
  requires_python = '>=3.6.0',
  url = 'https://github.com/srijan14/text-translation',
  download_url = 'https://github.com/srijan14/text-translation/archive/v_0.1.tar.gz',
  keywords = ['TEXT TRANSLATION', 'MACHINE TRANSLATION'],
  install_requires=['certifi==2019.9.11', 'chardet==3.0.4', 'ConfigArgParse==0.15.1', 'idna==2.8',
                    'numpy==1.17.4', 'requests==2.22.0', 'sentencepiece==0.1.83', 'six==1.13.0',
                    'torch==1.3.1', 'torchtext==0.4.0', 'tqdm==4.38.0', 'urllib3==1.25.7'],
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
