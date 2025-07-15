from django.shortcuts import render,redirect
from .models import Spend
from django.db.models import Sum
from .forms import SpendForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models.functions import ExtractYear


# Create your views here.



@login_required
def delete_spend(request,id):
    spend=Spend.objects.get(pk=id)
    spend.delete()

    return redirect('spending')

@login_required
def create_spend(request):
    message=''
    form=SpendForm()
    if request.method=='POST':
        print(request.POST)
        form=SpendForm(request.POST)
        spend=form.save(commit=False)
        spend.user=request.user
        spend.save()
        message='建立成功'
        return redirect('spending')

    return render(request,'spend/create_spend.html',{'form':form,'message':message})

@login_required
def spend(request,id):
    spend=None
    message=''
    try:
        spend=Spend.objects.get(id=id)
        if spend.user.id!=request.user.id:
            spend=None

            
        if request.method=='GET':
            form=SpendForm(instance=spend)
        
        if request.method=='POST':
            if request.POST.get('update'):
                form=SpendForm(request.POST,instance=spend)
                if form.is_valid():
                    spend=form.save(commit=False)
                    spend.user=request.user
                    spend.save()
                    message='更新成功'
            if request.POST.get('delete'):
                spend.delete()
                return redirect('spending')

    except Exception as e:
        print(e)
        message='更新失敗'
    return render(request,'spend/spend.html',{'spend':spend,'form':form,'message':message})


def spending(request):
    spends = None
    total_amount = 0
    years = []  
    selected_year = None
    selected_category = 'all'  # 預設顯示所有類型
    user = request.user
    if "year" in request.POST:
        now = int(request.POST["year"])
    else:
        now = int(datetime.now().strftime("%Y"))
        
    if user.is_authenticated:
        # 取得所有不同的年份，並確保年份排序
        years = list(Spend.objects.filter(user=user)
                     .annotate(year=ExtractYear('Creation_date'))
                     .values_list('year', flat=True)
                     .distinct()
                     .order_by('year'))

        # 從 POST 請求中獲取年份和類別，若無則使用預設值
        if request.method == "POST":
            selected_year = int(request.POST.get('year', datetime.now().year))
            selected_category = request.POST.get('category', 'all')
        else:
            selected_year = datetime.now().year
        
        # 確保所選年份是有效的（避免當前年份沒有資料時，選擇到錯誤的年份）
        if not years or selected_year not in years:
            selected_year = years[0] if years else datetime.now().year

        # 篩選該年紀錄
        filter_conditions = {'user': user, 'Creation_date__year': selected_year}
        if selected_category != 'all':
            filter_conditions['category'] = selected_category
        
        spends = Spend.objects.filter(**filter_conditions).order_by('Creation_date')
        
        # 計算該年該類型的花費總和
        total_amount = spends.aggregate(Sum('amount'))['amount__sum'] or 0


    return render(request, 'spend/spending.html', {
        'spends': spends,
        'total_amount': total_amount,
        'years': years,
        'year_now': now,
        'selected_year': selected_year,
        'selected_category': selected_category,
        'categories': Spend.category_choices,  # 顯示所有類型的選項
    })




        


    
