from django import forms

class MainForm(forms.Form):

    최종강화단계=forms.IntegerField()
    _1강가격=forms.IntegerField(min_value=0)
    _2강재료값=forms.IntegerField(required=False)
    _3강재료값=forms.IntegerField(required=False)
    _4강재료값=forms.IntegerField(required=False)
    _5강재료값=forms.IntegerField(required=False)
    _6강재료값=forms.IntegerField(required=False)
    _7강재료값=forms.IntegerField(required=False)
    _8강재료값=forms.IntegerField(required=False)
    _9강재료값=forms.IntegerField(required=False)
    _10재료값강=forms.IntegerField(required=False)