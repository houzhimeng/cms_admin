
# Create your views here.


from django.shortcuts import HttpResponse,render,redirect
from django.views import View
from app02 import models
import os

# Create your views here.

# USER_DICT = {
#          'k1': 'root1',
#          'k2': 'root2',
#          'k3': 'root3',
#          'k4': 'root4',
#          'k5': 'root5',
# }

USER_DICT = {
         '1': {'name':'root1','email':'root@live.com'},
         '2': {'name':'root2','email':'root@live.com'},
         '3': {'name':'root3','email':'root@live.com'},
         '4': {'name':'root4','email':'root@live.com'},
         '5': {'name':'root5','email':'root@live.com'},
}

USER_LIST = [
    {'name': 'root'},
    {'name': 'root'},
    {'name': 'root'},
    {'name': 'root'},
    {'name': 'root'},
]

def index(request):
    print(request.path_info)
    return render(request,'index.html',{'user_dict': USER_DICT})

def detail(request,nid):
    # return HttpResponse(nid)
    # # nid = request.GET.get('nid')
    detail_info = USER_DICT[nid]
    return render(request,'detail.html', {'detail_info':detail_info})

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # v = request.POST.get('gender')
        # print(v)

        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        # obj = models.UserInfo.objects.filter(username=u, password=p).count()  # 获取个数
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request, 'login.html')
        # if u == 'root' and p == '123':
        #     return redirect('/index')
        # else:
        # v = request.POST.getlist('favor')
        # v = request.POST.get('fafafa')
        # obj = request.FILES.get('fafafa')
        # file_path = os.path.join('upload', obj.name)
        # f = open(file_path, mode="wb")
        # for i in obj.chunks():
        #     f.write(i)
        # f.close()
        # print(obj)

        # return render(request,'login.html')
    else:
        return redirect('/index')

def orm(request):
    #增
    # models.UserInfo.objects.create(
    #     username="dsd",
    #     password="hhhhhrrew"
    # )

    #查
    # result = models.UserInfo.objects.filter(username='hou',password='123')
    # for row in result:
    #     print(row.id,row.username,row.password)

    #删
    # models.UserInfo.objects.filter(id=4).delete()

    #更新
    # models.UserInfo.objects.filter(id=3).update(password='999')

    return HttpResponse('orm')

class Home(View):

    def dispatch(self, request, *args, **kwargs):
        print('before')
        result = super(Home,self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):
        print(request.method)
        return render(request,'home.html')
