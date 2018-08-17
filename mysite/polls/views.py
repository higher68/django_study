from django.http import HttpResponse
# http://php6.jp/python/2011/01/21/string_format/
# %の意味について文字列中の%sの部分が、後ろに与えられた引数で置換される。
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id
# Create your views here.
