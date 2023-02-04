#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class Introduction:

    #クラス内に作られた式は属性値。呼び出し方は.explain
    explain = 'このクラスは.say("言葉")を入れるとprint文を実行する'

    #クラス内に作られた関数はメソッド。メソッドを定義する時、第1引数として必ずselfを指定する。指定なしだとエラー。
    def say(self,word):
        print(word)


#Introductionクラスを継承する
class Inheritance(Introduction):


    explain = 'このクラスはIntroductionを継承して作られました'
    extra   = 'この属性はInheritanceで新たに追加されました'

    def hello(self):
        print("Hello World")


#================Introductionクラスを動かす==========================================================

#クラスを変数に入れる。この変数をオブジェクトと言う。
intro   = Introduction()

#メソッドを実行させる。()を忘れずに。引数が必要なので、()内に"こんにちは"を入れる
intro.say("こんにちは")

#属性を参照する時、()は不要。
print(intro.explain)



#======Introductionクラスを継承して作られた、Inheritanceクラスを動かす===============================

#クラスを継承したクラスでオブジェクトを作る
inheri  = Inheritance()

#属性を参照する。(継承元の属性値が上書きされている。)
print(inheri.explain)

#新しく追加された属性を参照する。
print(inheri.extra)

#新しく定義したメソッドを実行。
inheri.hello()

#継承したメソッドが未指定の場合引き継がれる
inheri.say("こんにちは。継承元Introduction内に定義された.say()メソッドが残っているので発言できるよ")


#======問題==========================================================================================

# 問1:Inheritanceクラスにsayメソッドを記述した場合、どうなる？


# 答え: Introductionクラスから継承したsayメソッドがInheritanceクラス内でオーバーライドされる


# 問2:Introductionクラスのオブジェクトから.hello()メソッドを実行した時、どうなる？


# 答え: Introductionクラス内には.hello()メソッドは無いので、エラーになる。


# 問3:この状態で、IntroductionクラスはInheritanceクラスを継承できる？


# 答え: できない。継承する側、継承される側は常に一方向であるため。InheritanceクラスがIntroductionクラスを継承している状態で、その逆は両立できない。


