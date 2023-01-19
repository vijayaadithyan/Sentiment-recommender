from django.shortcuts import render
import pandas as pd
from SentiRecom import settings
from recommender.util import SentimentRecommender

# Create your views here.
import os

def indexpage(request):
    data = pd.read_csv(os.path.join(settings.BASE_DIR, 'recommender/data/sample30.csv'))
    # rest of the code

def indexpage(request):
    data=pd.read_csv('recommender/data/sample30.csv')
    usernames=list(data['reviews_username'])
    usernames=list(set(usernames))

    sent_reco_model = SentimentRecommender()
    
    if request.method == 'POST':
        user=request.POST.get('usernamesfield')
    
        sent_reco_output = sent_reco_model.top5_recommendations(user)
        return render(request, 'recommender/output.html',{'result':sent_reco_output})


    return render(request, 'recommender/index.html',{
        'usernames': usernames
    })