from setuptools import setup, find_packages

setup(
    name="Topsis-Ishita-102317272",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
    "console_scripts": [
        "topsis=topsis_ishita_102317272.topsis:main"
    ]
}
,
    author="Ishita Singh Oberoi",
    description="TOPSIS implementation using Python",
)