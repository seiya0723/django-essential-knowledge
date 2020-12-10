#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#manage.pyから呼び出されるので、同一ディレクトリを意味する.をファイル名の前に書く
from .models import models_intro

def views_intro():
    print("私はビューです。Djangoではサーバー側の処理(DBアクセス、ページレンダリング)を担当しています。")

    print("\n=================DBにアクセスするため、models.pyをimportして実行します。===================")

    models_intro()

    print("=================上記のmodels.pyの自己紹介はviews.pyによって呼び出されました=================\n")



