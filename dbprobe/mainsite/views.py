
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Newsletter, Crew, Modules, Newsletter, CrewSpec, Specializations, News, Research, CrewRes
from .forms import TourismForm, NewsletterForm, ResearchForm, NewsForm
from django.core.mail import send_mail

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def index(request):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='dbcoursework@gmail.com', # https://support.google.com/accounts/answer/6010255
            message="""
                You Signed Up to Receive the Latest Research News.
                """, # Emmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm            
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
            # return redirect('index')
    else:
        newsletter_form = NewsletterForm()

    

    return render(request, 'mainsite/index.html', { 'newsletter_form': newsletter_form })
    

def contact(request):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()
    
    return render(request, 'mainsite/Contact.html', { 'newsletter_form': newsletter_form })

# Emmmmmmmmmm news research select, moving between news

def news(request):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST

    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()

    news_q = News.objects.order_by('-n_date')[:3] # or res.id
    res_q = Research.objects.filter(r_status='finished')
    context = {
        'res_q': res_q,
        'news_q': news_q,
        'newsletter_form': newsletter_form
        }
    return render(request, 'mainsite/News.html', context)

def news_list(request, from_news, to_news):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
             newsletter_form.save()
             send_mail(
             subject='Test sub',
             from_email='blard.zixel@gmail.com',
             message="""
                 You Signed Up to Receive the Latest Research News.
                 """,
             recipient_list=[newsletter_form.cleaned_data['s_mail']]
             )
    else:
         newsletter_form = NewsletterForm()
    
    news_q = News.objects.order_by('-n_date')[from_news:to_news] # or res.id
    
    context = {
         'news_q': news_q,
         'newsletter_form': newsletter_form
         }
    return render(request, 'mainsite/News_res.html', context)



def crew(request):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()
    
    active_crew = Crew.objects.filter(p_status='working')
    specializations_list = Specializations.objects.all()
    crew_spec_list = CrewSpec.objects.all()

    # CrewSpec, Specializations

    context = {
        'active_crew': active_crew,
        'specializations_list': specializations_list,
        'crew_spec_list': crew_spec_list,
        'newsletter_form': newsletter_form
        }
    return render(request, 'mainsite/Crew.html', context)


 

def modules(request):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()
    
    active_modules = Modules.objects.filter(mod_status='working')
    context = {
        'active_modules': active_modules,
        'newsletter_form': newsletter_form
        }
    return render(request, 'mainsite/Modules.html', context)

def research(request):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()
    
    return render(request, 'mainsite/Research.html', { 'newsletter_form': newsletter_form })



def tourism(request):
    tourism_apply = request.method == 'POST' and 'tour_apply_btn' in request.POST
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST

    if tourism_apply:
        tourism_form = TourismForm(data=request.POST)
        if tourism_form.is_valid():
            tourism_form.save()
            return redirect('index')
    else:
        tourism_form = TourismForm()

    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()
    
    return render(request, 'mainsite/Tourism.html', {
        'tourism_form': tourism_form,
        'newsletter_form': newsletter_form
    }) 


def propose(request):
    research_apply = request.method == 'POST' and 'research_apply_btn' in request.POST
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST

    if research_apply:
        data = request.POST.copy()
        data['r_status'] = 'pending valid'
        research_form = ResearchForm(data=data)
            
        if research_form.is_valid():
            
            # Data truncated for column
            #return redirect(research_form.r_status)

            research_form.save()
            return redirect('index')
    else:
        research_form = ResearchForm()


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()
    
    return render(request, 'mainsite/Propose.html', {
        'research_form': research_form,
        'newsletter_form': newsletter_form
    })




def research_news(request, research_id):
    newsletter_apply = request.method == 'POST' and 'newsletter_apply_btn' in request.POST


    if newsletter_apply:
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            send_mail(
            subject='Test sub',
            from_email='blard.zixel@gmail.com',
            message="""
                You Signed Up to Receive the Latest Research News.
                """,
            recipient_list=[newsletter_form.cleaned_data['s_mail']]
            )
    else:
        newsletter_form = NewsletterForm()
    
    news_q = News.objects.filter(res=research_id) # or res.id
    
    context = {
        'news_q': news_q,
        'newsletter_form': newsletter_form
        }
    return render(request, 'mainsite/News_res.html', context)



@login_required
def profile(request):
    return render(request, 'mainsite/Personnel/Profile.html')

@login_required
def Res_pending(request):
    take_res = request.method == 'POST' and 'take_btn' in request.POST
    res_q = Research.objects.filter(r_status='pending team') # Or in progress not by current_user

    

    if take_res:
        for res in res_q:
            if int(request.POST["take_btn"]) == res.id:   

                current_user = request.user
                
                q = CrewRes(crew = current_user.profile.crew , res= res)
                q.save()

                Research.objects.filter(pk=res.id).update(r_status='in progress')
                
                return redirect('profile')

    context = {
        'res_q': res_q
        }
    return render(request, 'mainsite/Personnel/Res_pending.html', context)

@login_required
def Res_progress(request):

    finish_res = request.method == 'POST' and 'finish_btn' in request.POST


    res_q = Research.objects.filter(r_status='in progress') # in progress only by current_user

    

    if finish_res:
        for res in res_q:
            if int(request.POST["finish_btn"]) == res.id:   
                
                Research.objects.filter(pk=res.id).update(r_status='finished')
                
                return redirect('profile')

    context = {
        'res_q': res_q
        }
    return render(request, 'mainsite/Personnel/Res_progress.html', context)

@login_required
def Res_finished(request):

    # finish_res = request.method == 'POST' and 'finish_btn' in request.POST

    # current_user = request.user


    # res_q = Research.objects.filter(r_status='in progress') # why im doing this....

    

    # if finish_res:
    #     for res in res_q:
    #         if int(request.POST["finish_btn"]) == res.id:   
                
    #             Research.objects.filter(pk=res.id).update(r_status='finished')
                
    #             return redirect('profile')

    # context = {
    #     'res_q': res_q
    #     }
    # return render(request, 'mainsite/Personnel/Res_progress.html', context)


    return render(request, 'mainsite/Personnel/Res_finished.html')

from django.utils import timezone

@login_required
def News_post(request):

    news_post = request.method == 'POST' and 'news_post_btn' in request.POST


    current_user = request.user

    if news_post:
        data = request.POST.copy()

        data['n_date'] = timezone.now()
        
        data['author'] = current_user.profile.crew.id
    
        news_form = NewsForm(data=data)
            
        if news_form.is_valid():
            
            news_form.save()

            # send_mail(
            # subject='Test sub',
            # from_email='blard.zixel@gmail.com',
            # message="""
            #     You Signed Up to Receive the Latest Research News.
            #     """,
            
            # recipient_list=[newsletter_form.cleaned_data['s_mail']]
            # )
            return redirect('profile')
    else:
        news_form = NewsForm()

    context = {
        'news_form': news_form

        }
    return render(request, 'mainsite/Personnel/News_post.html', context)



def logout_view(request):
    logout(request)
    return redirect('login')


##############

    