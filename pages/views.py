from django.shortcuts import render, redirect, reverse
from django.views.generic import  ListView, DetailView, TemplateView, FormView
from core.models import *
from taggit.models import Tag
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from pages.forms import CommentForm,ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError





# Create your views here.

#   HOME   CONTENTS
class HomePageView(ListView):
    template_name = 'pages/index.html'
    model = AboutMeModel
    context_object_name = "about_me"

    # def get_queryset(self):
    #     context_object_name = AboutMeModel.objects.all()
    #     return context_object_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = ServicesModel.objects.all().order_by('id')
        context["progress"] = ServiceRatingModel.objects.all().order_by('id')
        context["portfolios"] = PotfolioModel.objects.all().all().order_by('id')
        context["news"] = NewsModel.objects.all().order_by('-id')[:2]
        return context

#   RESUME CONTENTS
class ResumeListView(ListView):
    template_name = 'pages/resume_lists.html'
    model = AboutMeModel
    context_object_name = 'aboutme'

    def get_queryset(self):
        context_object_name = AboutMeModel.objects.get(id=1)
        return context_object_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experiences"] = Experiences.objects.all()
        context["schools"] = Schools.objects.all()
        context["progress"] = ServiceRatingModel.objects.all()
        return context

#    SERVICES CONTENTS
class ServiceListView(ListView):
    template_name = 'pages/service_lists.html'
    model = ServicesModel
    context_object_name = 'services'


class ServicesDetailView(DetailView):
    model = ServicesModel
    template_name = "pages/service_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # service = self.get_object().service
        slug = self.kwargs["slug"]

        more_service = ServicesModel.objects.all().exclude(slug=slug)
        questions = PotfolioQuestionModel.objects.all()

        context.update(
            {
                "more_service":more_service,
                "questions":questions
            }
        )

        return context


#    PORTFOLIOS  CONTENTS
class PortfolioListView( ListView):
    model = PotfolioModel
    template_name = 'pages/portfolio_list.html'
    context_object_name = "portfolios"

class PortfolioDetailsView(DetailView):
    model = PotfolioModel
    template_name = 'pages/potfolio_detail.html'
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.filter(potfolio=self.object)
        context['tags'] = Tag.objects.filter(potfoliomodel__slug=self.kwargs.get('slug'))
        context['aboutme'] = AboutMeModel.objects.get(id=1)
        return context



#   BLOG CONTENTS
class PortfolioBlogView(LoginRequiredMixin, ListView):
    login_url = 'account/signin/'
    template_name = 'pages/portfolio_blog.html'
    paginate_by = 3
    model = PortfolioBlogModel
    context_object_name = "blogs"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['blogs'] =self.model.objects.all()
        context['recent_posts'] = self.model.objects.all().order_by('-id')[:4]
        context['categories'] = CategoryModel.objects.all()
        # context['tags'] = Tag.objects.filter(portfolioblogmodel__slug=self.kwargs.get('slug'))
        return context

#  category
class CategoryListView(LoginRequiredMixin, ListView):
    login_url = '/account/signin/'
    model = CategoryModel
    template_name = 'pages/categories.html'
    context_object_name = "categories"
    paginate_by =5

    def get_queryset(self):
        return PortfolioBlogModel.objects.filter(category_id=self.kwargs['cat_id'])


class SearchResultsView(ListView):
    login_url = '/account/signin/'
    model = PortfolioBlogModel
    template_name = 'pages/search.html'
    context_object_name = "blogs"

    def get_queryset(self): 
        query = self.request.GET.get("query")
        object_list = PortfolioBlogModel.objects.filter(
            Q(name__icontains=query) 
        )
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = self.model.objects.all().order_by('-id')[:4]
        return context

class PortfolioBlogDetailView(LoginRequiredMixin, DetailView):
    login_url = '/account/signin/'
    model = PortfolioBlogModel
    template_name = 'pages/portfolioblog_detail.html'
    context_object_name = "blogs"


    comment_form = CommentForm()
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post = self.get_object()
            comment_form.instance.author = request.user
            comment_form.instance.post = post
            comment_form.save()

            return redirect(reverse("blogdetail", kwargs={
                'slug':post.slug
            }))




    def get_context_data(self, **kwargs):
        qs =  CommentsModel.objects.filter(post=self.object, active=True)
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.filter(blogs = self.object)
        context['comments'] = qs.order_by('-created', '-updated')
        context['comment_form'] = self.comment_form
        
        return context

# class CommentCreateView( CreateView):
#     # template_name = 'pages/portfolioblog_detail.html'
#     form_class = CommentForm
#     model = CommentsModel

#     fields = ['body',]

#     def form_valid(self, form):
#         post  = self.get_object()
#         form.instance.post = post   
#         form.instance.name = self.request.user
#         return super().form_valid(form.save)


#NEWS
class NewsDetails(DetailView):
    model = NewsModel
    template_name = 'pages/news_details.html'
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.filter(news = self.object)

        return context



class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'pages/success.html'

# def contact(request):
#      if request.method == "GET":
#         form = ContactForm()
#      else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data["subject"]
#             email = form.cleaned_data["email"]
#             phone = form.cleaned_data["phone"]
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(f'{subject} phone:{phone}', message, email, ["mastergentility5@gmail.com"])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             return redirect("success")
#      return render(request, 'pages/contact.html',{'form':form})


# def successView(request):
#     return HttpResponse("Success! Thank you for your message.")








   

   






