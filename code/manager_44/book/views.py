from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('ok')


##################添加

from book.models import BookInfo, PeopleInfo

book = BookInfo(
    name="python入门",
    pub_date='2010-1-1',
)
book.save()

PeopleInfo.objects.create(
    name='itheima',
    book=book
)
#####################修改
preson = PeopleInfo.objects.get(name='itheima')
preson.name = 'itcast'
preson.save()

PeopleInfo.objects.filter(name='itcast').update(name="传智播客")
#################删除
person = PeopleInfo.objects.get(name='传智播客')
person.delete()

BookInfo.objects.filter(name="python入门").delete()

#################查询
BookInfo.objects.filter(id=1)
BookInfo.objects.get(id=1)
# 查询编号为1的图书
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
BookInfo.objects.get(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

##############F-Q对象
from django.db.models import F, Q
BookInfo.objects.filter(readcount__gt=F('commentcount'))
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)

###############Q
BookInfo.objects.filter(readcount__gt=20,id__lt=3)
BookInfo.objects.filter(readcount__gt=20)
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
BookInfo.objects.filter(~Q(id=3))


#############聚合函数
from django.db.models import Sum,Max,Avg,Count,Min
BookInfo.objects.count()
BookInfo.objects.aggregate(Sum('readcount'))
BookInfo.objects.all().order_by('id')
BookInfo.objects.all().order_by('-id')
