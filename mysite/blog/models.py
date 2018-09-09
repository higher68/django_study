from django.db import models
from django.utils import timezone
# Create your models here.
# オブジェクト定義
# filed：入力項目？レコードがデータベースに登録された１件分のデータ？
# models.Modelを引数にすると、なんかDjangoがデータベースに保存してくれるらしい
class Post(models.Model):
    # プロパティ設定
    author = models.ForeignKey('auth.User')  # 他のモデルへのリンク
    title = models.CharField(max_length=200)  # テキスト数を定義するフィールド
    text = models.TextField  # 無制限の長いテキスト用のフィールド
    created_date = models.DateTimeField(default=timezone.now)  # 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)


    # ブログを公開するメソッド？
    def publish(self):
        self.published_date = timezone.now()
        self.save()

        
    # ポストの表題のテキストを出力
    def __str__(self):
        return self.title
