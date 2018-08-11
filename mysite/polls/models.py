from django.db import models
# スキーマは、データベースで多数のテーブルを作るときに、
# テーブルごとに分類するための仕組み：ディレクトリに相当
# テーブル(表)とは、作成されたファイルに相当
# このコードによって、アプリケーションのデータスキーマを作成できる
# つまりcreate table文を実行できる
# questionやchoiceオブジェクトにpythonからアクセスするためのデータベースAPIを作成できる
# API：Application programming interface
# アプリとアプリの間でデータをやり取りする方法(google mapとかは
# APIをbingmapとかから取得している。
# Web APIはhttpでリクエストを送受信する仕組み
# データは一般的にjsonやxmlが使われている
# SaaS(Software as a Service)からデータをやり取りをする際にとても重要です。
# アプリ  →(このデータをください(HTTP))　webサーバ
# アプリ　 ← (データだけをどうぞ(HTTP)json,xml形式) Webサーバ 
# SaaSとは、ネット経由でソフトを利用できる形態。
# Create your models here.
# 2つのモデルを作成、モデル＝1:データベースのレイアウト
# 2:データベースのメタデータとなっている。
# 個々のクラス変数はデータベースのフィールド
class Question(models.Model): 
    question_text = models.CharField(max_length=200) # 文字のフィールド
    pub_data = models.DateTimeField('date published')  # 日時のフィールド
    # 上の二つのフィールド指定で、どんなデータ型を記憶されるかをdjangoに教える
    # Question.pub_dataの中身は、人間に可読なフィールド名
    # Fieldクラスの中には必須の引数がいる。max_lengthがそれ。
class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    # ForeignKeyは依存関係にある2つの表を結びつける
    # 入力変数の値の候補を指定する
    # 今回はChoiceが1つのQuestionに関連づけられる
    choice_text = models.CharField(max_lngth=200)
    votes = models.IntegerField(default=0)
    # defaultはオプション引数
