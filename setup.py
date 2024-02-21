from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
        name="boodle",
        version="0.0.1",
        description="Command Line Money Management Tool",
        long_description=long_description,
        author="Owen Schaefer",
        author_email="owens0506@gmail.com",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Money :: Bugeting",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3 :: Only",
        ],
        package_dir={"": "src"},
        packages=find_packages(where="src"),
        install_requires=[
            "pyyaml",
        ],
        entry_points={
            "console_scripts": [
                "boodle=boodle:main",
            ],
        },
        project_urls={
            "Source": "https://github.com/refeahcs00/boodle",
            "Bug Reports": "https://github.com/refeahcs00/boodle/issues",
        }

)
