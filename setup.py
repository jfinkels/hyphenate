from setuptools import setup

setup(
    name='hyphenate',
    version='1.0.0.dev0',
    description='Determine hyphenation breaks in English words',
    long_description=__doc__,
    author='Ned Batchelder',
    maintainer='Jeffrey Finkelstein',
    maintainer_email='jeffrey.finkelstein@gmail.com',
    url='https://github.com/jfinkels/hyphenate',
    download_url='https://pypi.python.org/pypi/hyphenate',
    py_modules=['hyphenate'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        # TODO Test me with more Python versions!
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing',
    ],
    license='CC0 1.0',
    platforms='any',
    test_suite='test_hyphenate',
)
