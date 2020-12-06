import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='akv',
    version='0.0.1',
    author='Casper Lehmann',
    author_email='casperlehmann@gmail.com',
    description='Simple access to Azure Key Vault Secrets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/casperlehmann/akv',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'azure-identity',
        'azure-keyvault-secrets',
    ],
)
