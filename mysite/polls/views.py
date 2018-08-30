from django.http import HttpResponse
# http://php6.jp/python/2011/01/21/string_format/
# %の意味について文字列中の%sの部分が、後ろに与えられた引数で置換される。
# viewの役割・・・１：リクエストされたページのコンテンツを含むオブジェクトを返す
# ２：Http404のような例外の送出
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    # 並べ替え
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # modelclass.modelmanager.method()という形でクエリを実行
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list])
    # 区切り文字.join(list)として、区切り文字を入れて連結できる
    # システム上の最新5件の質問をカンマで区切り、日付順に表示
    # rendering表示用のデータを元に、内容を整形して表示すること
    # マッピング：対応づけること？
    # テンプレートを指定のコンテキストでレンダリングし、そのHttpResponseオブジェクトを返す。
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here
