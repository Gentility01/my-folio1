from django.urls import path
from pages import views


urlpatterns = [
    path('tag/<slug:tag_slug>', views.PortfolioDetailsView.as_view(), name="post_by_tag"),


    path('', views.HomePageView.as_view(), name='homepage'),
    path("services", views.ServiceListView.as_view(), name = 'service'),
    path("detail/<slug:slug>/",views.ServicesDetailView.as_view(),name="servicedetail"),
    path("resume", views.ResumeListView.as_view(), name='resume'),
    path("portfolios", views.PortfolioListView.as_view(), name="portfolio_list"),
    path("portfolio/<slug:slug>/",views.PortfolioDetailsView.as_view(),name="potfoliodetail"),
    path('blogs', views.PortfolioBlogView.as_view(), name='blogs'),
    path("categories/<int:cat_id>/", views.CategoryListView.as_view(), name="categories" ),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("blog/<slug:slug>", views.PortfolioBlogDetailView.as_view(), name="blogdetail"),
    path("news/<slug:slug>", views.NewsDetails.as_view(), name="newsdetail"),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('success', views.ContactSuccessView.as_view(), name='success'),

  
    
   
]