from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zoopy',
    version='0.0',
    author='Nikita Bakutov',
    author_email='nikitabakutov2008@gmail.com',
    description='A Python library for animal data analysis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/droyti46/zoopy',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.2.0',
        'matplotlib>=3.9.0',
        'tqdm>=4.66.0',
        'Levenshtein>=0.26.0',
        'numpy>=1.26.4',
        'torch>=2.4.0',
        'torchvision>=0.19.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires=">=3.8",
    include_package_data=True,
)