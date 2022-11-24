from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    #render - связывеет запросы, страницы и переменные
    #в render можно отправить третий аргумент - это контекст (context)
    #context указывается в виде словаря, где ключ - это имя переменной в html,
    # а значение ключа - это значение этой переменной
def reverse(request):
    user_text = request.GET['username']
    reversed_text = user_text[::-1]
    return render(request,
                  'reverse.html',
                  {'word': reversed_text}
                  )