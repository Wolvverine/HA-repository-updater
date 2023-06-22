"Home Assistant add-ons repository updater setup."
from setuptools import find_packages, setup

from repositoryupdater import APP_DESCRIPTION, APP_NAME, APP_VERSION

setup(
    name=APP_NAME,
    version=APP_VERSION,
    author="Michał Panasiewicz",
    author_email="wolvverinepld@gmail.com",
    description=APP_DESCRIPTION.split("\n")[0],
    long_description=APP_DESCRIPTION,
    license="MIT",
    url="https://github.com/Wolvverine/HA-repository-updater",
    keywords=[
        "addons",
        "repository",
        "home assistant",
        "home-assistant",
        "add-ons",
        "wolvverinepld",
    ],
    platforms="any",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=[
        "click==8.1.3",
        "crayons==0.4.0",
        "emoji==2.5.1",
        "GitPython==3.1.31",
        "Jinja2==3.1.2",
        "PyGithub==1.58.2",
        "python-dateutil==2.8.2",
        "PyYAML==6.0",
        "semver==3.0.1",
    ],
    entry_points="""
        [console_scripts]
            repository-updater=repositoryupdater.cli:repository_updater
            repository-updater-git-askpass=repositoryupdater.cli:git_askpass
    """,
)
