from django.http import HttpResponse
# http://php6.jp/python/2011/01/21/string_format/
# %の意味について文字列中の%sの部分が、後ろに与えられた引数で置換される。
# viewの役割・・・１：リクエストされたページのコンテンツを含むオブジェクトを返す
# ２：Http404のような例外の送出
from django.http import HttpResponse

def index(request):
    # 並べ替え
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # modelclass.modelmanager.method()という形でクエリを実行
    output = ', '.join([q.question_text for q in late_question_list])
    # 区切り文字.join(list)として、区切り文字を入れて連結できる
    # システム上の最新5件の質問をカンマで区切り、日付順に表示
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here
