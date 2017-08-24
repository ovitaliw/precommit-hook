#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from app.extras import template
import os


class Exec:
    @staticmethod
    def add_pre_commit():

        # if .git directory exists
        if os.path.isdir(os.path.join(os.getcwd(), ".git")):
            # make hook directory if not exists
            if not os.path.isdir(os.path.join(os.getcwd(), ".git/hooks")):
                os.system("mkdir -p .git/hooks")
        else:
            os.system("git init")

        # finally copy and set permissions
        with open('.git/hooks/pre-commit', 'wb') as f:
            f.write(template.encode())
            os.system("sudo chmod +x .git/hooks/pre-commit")
        print("Precommit added successfully, continuing ...")
        return True


class Post_install(install):

    def run(self):
        install.run(self)
        Exec.add_pre_commit()


class Post_develop(develop):

    def run(self):
        develop.run(self)
        Exec.add_pre_commit()


class Post_egg_info(egg_info):

    def run(self):
        egg_info.run(self)
        Exec.add_pre_commit()
