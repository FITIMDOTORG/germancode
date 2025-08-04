from setuptools import setup, find_packages

setup(
    name="germancode",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["lark", "click"],
    entry_points={
        "console_scripts": [
            "deutsch = germancode.cli.deutsch:deutsch"
        ]
    },
)
