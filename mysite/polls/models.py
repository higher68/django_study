from django.db import models

# Create your models here.
# 2つのモデルを作成、モデル＝1:データベースのレイアウト
# 2:データベースのメタデータとなっている。
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
