#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#既にviews.pyがmodels.pyをimportしているため、models.pyはviews.pyをimportしてはならない。エラーになる。

def models_intro():
    print("私はmodels.pyです。DjangoではDBの定義を主に行っています。views.pyがDBにアクセスする時に私が参照されます。")


