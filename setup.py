import sys
from distutils.core import setup


VERSION_FILE = 'codebug_i2c_tether/version.py'
PY3 = sys.version_info[0] >= 3


def get_version():
    if PY3:
        version_vars = {}
        with open(VERSION_FILE) as f:
            code = compile(f.read(), VERSION_FILE, 'exec')
            exec(code, None, version_vars)
        return version_vars['__version__']
    else:
        execfile(VERSION_FILE)
        return __version__


setup(
    name='codebug_i2c_tether',
    version=get_version(),
    description='CodeBug I2C Tether module.',
    author='Thomas Preston',
    author_email='thomas.preston@openlx.org.uk',
    license='GPLv3+',
    url='https://github.com/codebugtools/codebug_i2c_tether',
    packages=['codebug_i2c_tether'],
    long_description=open('README.md').read() + open('CHANGELOG').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or "
        "later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='codebug raspberrypi raspberry pi openlx',
)
