from django.shortcuts import render
from django.views.generic import View
from . import forms
import random

class HomeView(View):
    def get(self, request):
        return render(request, "upgrades/tutorial.html")

class MainView(View):

    def get(self, request):


        form = forms.MainForm(request.GET)

        if form.is_valid():
            n= form.cleaned_data.get("최종강화단계")
            price1= form.cleaned_data.get("_1강가격")
            price2= form.cleaned_data.get("_2강재료값")
            price3= form.cleaned_data.get("_3강재료값")
            price4= form.cleaned_data.get("_4강재료값")
            price5= form.cleaned_data.get("_5강재료값")
            price6= form.cleaned_data.get("_6강재료값")
            price7= form.cleaned_data.get("_7강재료값")
            price8= form.cleaned_data.get("_8강재료값")
            price9= form.cleaned_data.get("_9강재료값")
            price10= form.cleaned_data.get("_10재료값강")

            booli=0

            if n==2:
                if price1==None or price2==None:
                    booli=1

            elif n==3:
                if price1==None or price2==None or price3==None:
                    booli=1

            elif n==4:
                if price1==None or price2==None or price3==None or price4==None:
                    booli=1

            elif n==5:
                if price1==None or price2==None or price3==None or price4==None or price5==None:
                    booli=1

            elif n==6:
                if price1==None or price2==None or price3==None or price4==None or price5==None or price6==None:
                    booli=1

            elif n==7:
                if price1==None or price2==None or price3==None or price4==None or price5==None or price6==None or price7==None:
                    booli=1

            elif n==8:
                if price1==None or price2==None or price3==None or price4==None or price5==None or price6==None or price7==None or price8==None:
                    booli=1

            elif n==9:
                if price1==None or price2==None or price3==None or price4==None or price5==None or price6==None or price7==None or price8==None or price9==None:
                    booli=1

            elif n==10:
                if price1==None or price2==None or price3==None or price4==None or price5==None or price6==None or price7==None or price8==None or price9==None or price10==None:
                    booli=1

            else:
                booli=1

            price=[]

            if price2:
                price.append(price2)
            
            if price3:
                price.append(price3)

            if price4:
                price.append(price4)

            if price5:
                price.append(price5)
            
            if price6:
                price.append(price6)

            if price7:
                price.append(price7)

            if price8:
                price.append(price8)
            
            if price9:
                price.append(price9)

            if price10:
                price.append(price10)

            prob=[100, 81, 64, 50, 26, 15, 7, 4, 2]
            P=0

            def f(x):
                if x<=random.randrange(1, 101):
                    return 'F'
                else:
                    return 'T'

            k=1
            c=0
            
            if booli==1:
                result='숫자를 다시 입력하십시오(최종강화단계: 2~10, 해당 강화 단계까지의 재료값 모두 입력)'
            else:
                while True:
                    if f(prob[k-1])=='T':
                        P+=price[k-1]
                        c+=1
                        k+=1
                    else:
                        P+=price[k-1]
                        c+=1
                        k=1
                    if k==n:
                        break
                result='강회 시도 횟수: '+str(c)+'회'+'\n'+'총 비용: '+str(P+price1)+'BP'

            return render(request, "upgrades/main.html", {"form": form, "result": result})

        else:
            form = forms.MainForm(request.GET)
            return render(request, "upgrades/main.html", {"form": form})