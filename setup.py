from setuptools import setup

setup(
    name='sequencify.py',
    version='0.1.0.dev1',
    author='TitanSnow',
    author_email='tttnns1024@gmail.com',
    description='A module for sequencing tasks and dependencies',
    url='https://github.com/TitanSnow/sequencify.py',
    license='LGPLv2.1',
    platforms=['any'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['sequencify'],
    test_suite='tests.suite',
    zip_safe=True,
)
