from setuptools import find_packages, setup

package_name = "square_database_structure"

setup(
    name=package_name,
    version="2.6.0",
    packages=find_packages(),
    package_data={
        package_name: ["**/**/stored_procedures_and_functions/*.sql"],
    },
    install_requires=[
        "sqlalchemy>=2.0.23",
        "psycopg2-binary>=2.9.9",
    ],
    extras_require={
        "all": [
            "pytest>=8.0.0",
        ],
        "test": [
            "pytest>=8.0.0",
        ],
    },
    author="Parth Mukesh Mangtani",
    author_email="thepmsquare@gmail.com",
    description="database scheme for my personal server.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/thepmsquare/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
