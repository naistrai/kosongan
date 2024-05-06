import subprocess
import time
from random_word import RandomWords
r = RandomWords()
token = "pypi-AgEIcHlwaS5vcmcCJDJhNzM3NTI4LWZlNzItNGEyOS1iZjBmLTYyZmY2N2U3MzcxNAACKlszLCI3MmI2ODUyNC0zNzVhLTQyNDUtODI0ZC1mYzVlYzcyNTYzOGYiXQAABiAdCdVxJza7W0MKtjdAg6DVd-DQ-113DNtoTFQWn-A2Gg"

def install_pkg():
    completed_process = subprocess.run('pip install discorudo', text=True, shell=True, capture_output=True)

def git_create(name):
    # Running a shell pipeline
    completed_process = subprocess.run(
        "git clone https://github.com/defartsa23/python-library-quick-start.git &&\
        mv python-library-quick-start/ "+name+"/ && \
        cd "+name+" && \
        mv your-package/ "+name+"/ && \
        cp ../sample_main.py "+name+"/main.py",
        shell=True,
        text=True,
        capture_output=True
    )

def create_file(name):
    isi = "from distutils.core import setup\n\
from pathlib import Path\n\
this_directory = Path(__file__).parent\n\
long_description = (this_directory / 'README.md').read_text()\n\n\
setup(\n\
    name = '"+name+"',\n\
    packages = ['"+name+"'],\n\
    version = '1.1',\n\
    license='MIT',\n\
    description = '"+name+"',\n\
    long_description=long_description,\n\
    long_description_content_type='text/markdown',\n\
    author = 'Naistrai',\n\
    author_email = 'rizkynaistrai@gmail.com',\n\
    url = 'https://github.com/naistrai/"+name+"',\n\
    download_url = 'https://github.com/naistrai/"+name+"/archive/v_01.tar.gz',\n\
    project_urls={\n\
        'Documentation': 'https://github.com/naistrai/"+name+"',\n\
        'Funding': 'https://donate.pypi.org',\n\
        'Say Thanks!': 'http://saythanks.io/to/example',\n\
        'Source': 'https://github.com/naistrai/"+name+"/',\n\
        'Tracker': 'https://github.com/naistrai/"+name+"/issues',\n\
    },\n\
    keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],\n\
    install_requires=[\n\
            'validators',\n\
            'beautifulsoup4',\n\
            'discordautochat',\n\
            'discorudo',\n\
        ],\n\
    classifiers=[\n\
        'Development Status :: 3 - Alpha',\n\
        'Intended Audience :: Developers',\n\
        'Topic :: Software Development :: Build Tools',\n\
        'License :: OSI Approved :: MIT License',\n\
        'Programming Language :: Python :: 3',\n\
        'Programming Language :: Python :: 3.4',\n\
        'Programming Language :: Python :: 3.5',\n\
        'Programming Language :: Python :: 3.6',\n\
    ],\n\
     dependencies= [\n\
        'discordautochat',\n\
        'discorudo'\n\
    ]\n\
)"
    completed_process = subprocess.run('echo "'+isi+'" > '+name+'/setup.py', text=True, shell=True, capture_output=True)

def upload(name):
    completed_process = subprocess.run(
        "cd "+name+"/ &&\
        python setup.py sdist && \
        twine upload dist/* -u __token__ -p "+token,
        shell=True,
        text=True,
        capture_output=True
    )

# install_pkg()
# git_create('yuzutea')
# create_file('yuzutea')
# upload('yuzutea')
while True:
    txt = r.get_random_word() + 'z'
    print(f"Create :{txt}")
    git_create(txt)
    print(f"File :{txt}")
    create_file(txt)
    print(f"Upload :{txt}")
    upload(txt)
    print(f"Done!")
    time.sleep(60)