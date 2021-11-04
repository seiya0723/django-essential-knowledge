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


# 問2:introディレクトリの中にtestディレクトリを作り、その中にtest.pyを作り、test.pyがmodels.pyをimportするにはどのように書けばよいか？


# 問3:introディレクトリの中にtestディレクトリを作り、その中にdeepディレクトリを作り、その中にdeep.pyを作り、deep.pyがmodels.pyをimportするにはどのように書けばよいか？

