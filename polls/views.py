from django.http import HttpResponse


def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return HttpResponse("Hello, world. You're at the polls index.")
