#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#introディレクトリのviews.pyとmodels.pyをimport
from intro import views,models

print("私はmanage.pyです。私を実行して他のPythonファイル内の処理を呼び出します。")
views.views_intro()
models.models_intro()

"""
モジュールに関しては下記を参照
https://note.nkmk.me/python-relative-import/

"""


#====問題========================================

# 問1:introディレクトリ内にadmin.pyを作って、admin.pyがmodels.pyをimportするにはどのように書けばよいか？

# intro/admin.py を作り内容は下記

"""
from . import models

def admin_intro():
    print("====admin.py====")
    models.models_intro()
    print("====admin.py====")

"""

# このintro/admin.pyをmanage.pyから呼び出す。

from intro import admin

admin.admin_intro()



# 問2:introディレクトリの中にtestディレクトリを作り、その中にtest.pyを作り、test.pyがmodels.pyをimportするにはどのように書けばよいか？


# intro/test/test.py を作り内容は下記


"""
from .. import models 

def test_intro():
    print("====test.py====")
    models.models_intro()
    print("====test.py====")
"""

# このintro/test/test.pyをmanage.pyから呼び出す。

from intro.test import test

test.test_intro()


# 問3:introディレクトリの中にtestディレクトリを作り、その中にdeepディレクトリを作り、その中にdeep.pyを作り、deep.pyがmodels.pyをimportするにはどのように書けばよいか？

# intro/test/deep/deep.py を作り内容は下記

"""
from ... import models 

def deep_intro():
    print("====deep.py====")
    models.models_intro()
    print("====deep.py====")
"""

from intro.test.deep import deep

deep.deep_intro()


