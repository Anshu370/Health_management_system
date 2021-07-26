from setuptools import setup
import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name='HEALTH_MANAGEMENT',
    version='0.0.1',
    description='A health management system with all the basic functions. '
                'you can also create a program using tkinter using this library',
    author='Anshu Gupta',
    # url='https://github.com/Anshu370/PyMusic_Player',
    # long_description = long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['health manmagement python', 'health managemengt system', 'python health management', 'health management'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    py_modules=['HEALTH_MANAGEMENT'],
    package_dir={'': 'src'},
    install_requires=[
        'datetime'
    ]
)
