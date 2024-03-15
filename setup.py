from setuptools import find_packages
from setuptools import setup

setup(
    name='USDAssetBrowser',
    version="1.0.0",
    description="Studio asset browser for CIS7000",
    author="Michael Mason",
    author_email="micmas@seas.upenn.edu",
    url="https://github.com/micklemacklemore/USDAssetBrowser",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'assetbrowser = USDAssetBrowser.main:main'
        ]
    },
    install_requires=["pyqt5-tools >= 5.15"],
    python_requires=">=3.9,<3.10"
)
