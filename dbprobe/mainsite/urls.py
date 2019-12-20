from django.urls import path, include

from . import views

#app_name = 'mainsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('crew/', views.crew, name='crew'),
    path('modules/', views.modules, name='modules'),
    path('research/', views.research, name='research'),
    path('tourism/', views.tourism, name='tourism'),
    path('propose/', views.propose, name="propose"),

    path('signup/', include('django.contrib.auth.urls')),
    path('signup/login/profile_page/', views.profile, name='profile'),
    path('signup/Res_pending/', views.Res_pending, name='Res_pending'),
    path('signup/Res_progress/', views.Res_progress, name='Res_progress'),
    path('signup/Res_finished/', views.Res_finished, name='Res_finished'),
    path('signup/News_post/', views.News_post, name='News_post'),
    path('signup/logout_view/', views.logout_view, name='logout_view'),


    path('news/research_<int:research_id>', views.research_news, name='research_news'),
    path('news/<int:from_news>-<int:to_news>', views.news_list, name='news_list')

]

# accounts/profile