# URLconfをpollsディレクトリに作る。
# ビューを呼ぶためのURLが対応付けされる
from django.urls import path

from . import views
# path()
# アプリケーションの名前空間を設定、複数のアプリのビューを区別する。
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # 第一引数が、urlの情報、第二引数が、左の条件を満たす時に、参照するパス
    # 第３引数が、上記パターンの名前
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results,
    name = 'results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
