from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect,reverse
from app01.models import User,Customer
import json,datetime
# from app01.form import UserForm

# def required_login(func):
#     def inner(*args,**kwargs):
#         request = args[0]
#         if request.session.get('is_login'):
#             return func(*args,**kwargs)
#         else:
#             if request.is_ajax():
#                 response = {"state": False}
#                 return HttpResponse(json.dumps(response))
#             return redirect('/login/')
#     return inner
#
# @required_login
# def show_books(request):
#     book_list = Book.objects.all()
#     return render(request,'showcustomer.html',{'book_list':book_list})
#
# @required_login
# def add_books(request):
#     if request.method=='GET':
#         pulish_list = Publish.objects.all()
#         author_list = Author.objects.all()
#         return render(request, 'addbooks.html',{'pulish_list':pulish_list,'author_list':author_list})
#     else:
#         print(request.POST)
#         title = request.POST.get("title")
#         price = request.POST.get("price")
#         pub_date = request.POST.get("pub_date")
#         publish_id = request.POST.get("publish_id")
#         authors_id_list = request.POST.getlist("authors_id")
#         book_obj = Book.objects.create(title=title, price=price, publish_id=publish_id, pub_date=pub_date)
#         book_obj.authors.add(*authors_id_list)
#         return redirect("/books/")
#
# @required_login
# def del_books(request,nid):
#     response = {"state":True}
#     try:
#         Book.objects.filter(id=nid).delete()
#     except Exception:
#         response["state"] = False
#     return HttpResponse(json.dumps(response))
#
# @required_login
# def update_books(request,nid):
#     update_books_obj = Book.objects.filter(id = nid).first()
#     pulish_list = Publish.objects.all()
#     author_list = Author.objects.all()
#     if request.method == 'POST':
#         title = request.POST.get("title")
#         price = request.POST.get("price")
#         pub_date = request.POST.get("pub_date")
#         publish_id = request.POST.get("publish_id")
#         authors_id_list = request.POST.getlist("authors_id")
#         Book.objects.filter(id=nid).update(title=title, price=price, publish=publish_id, pub_date=pub_date)
#         update_books_obj.authors.set(authors_id_list)
#         return redirect("/books/")
#
#
#     return render(request, 'updatebooks.html', {'update_books_obj':update_books_obj,'pulish_list': pulish_list, 'author_list': author_list})
#
# @required_login
# def index(request):
#     return render(request,'index.html')
#

#
#
# def adduser(request):
#     if request.method=="POST":
#         form=UserForm(request.POST) #{"title":"AAA"}
#         print(form)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             print(name)
#             age = form.cleaned_data.get('age')
#             pwd = form.cleaned_data.get('pwd')
#             email = form.cleaned_data.get('email')
#             telphone = form.cleaned_data.get('telphone')
#             book_obj = User.objects.create(name=name,age=int(age),pwd=pwd,telphone=telphone,email=email)
#             return redirect('/login/')
#         else:
#             print(form.cleaned_data)
#             # print(form.errors) # {"email":["",....]}
#             # print(type(form.errors))
#             # print(form.errors.get("email")[0])       # {"email":["",....]}
#             # print(type(form.errors.get("email")))  # []
#             g_error=form.errors.get("__all__")
#             if g_error:
#                 g_error=g_error[0]
#             return render(request, "adduser.html", locals())
#     else:
#         form=UserForm()
#         return render(request, "adduser.html",locals())

def login(request):
    if request.method=='POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user_list = User.objects.filter(name = name,pwd=pwd)
        if user_list:
            user_obj = user_list.first()
            ret = redirect('/books/')
            request.session['is_login']=True
            request.session['name'] = name
            request.session['last_time']=datetime.datetime.now().strftime('%Y-%m-%d')
            user_obj.save()
            return ret
    return render(request,'login.html')

def logout(request):
    ret = redirect('/login/')
    request.session.flush()
    return ret

def showcustomer(request):
    querysetlist = []
    for i in customerlist:
        querysetlist.append(i)
    Customer.objects.bulk_create(querysetlist)

    return HttpResponse('')



