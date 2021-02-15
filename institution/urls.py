from django.urls import path
from institution.views import HomeView, AboutUsView, TeachersView, \
    DownloadsView, ContactView, SacredDatesView, NewsListView, \
    NewsDetailView, BranchesView, GenericPageView

app_name = 'institution'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContactView.as_view(), name='contact'),
    path('datas-sagradas/', SacredDatesView.as_view(), name='sacred-dates'),
    path('downloads/', DownloadsView.as_view(), name='downloads'),
    path('professores/', TeachersView.as_view(), name='teachers'),
    path('quem-somos/', AboutUsView.as_view(), name='about-us'),
    path('filiais/', BranchesView.as_view(), name='branches'),
    path('novidades', NewsListView.as_view(), name='news-list'),
    path('novidades/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('<int:slug>/', GenericPageView.as_view(), name='news-detail'),
]
