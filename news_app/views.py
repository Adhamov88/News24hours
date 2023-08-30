from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView

from .models import News, Category
from .forms import ContactForm
# Create your views here.


def ListViews(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news_list.html', context)


def detail_views(request, news):
    detail_list = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'detail_list': detail_list
    }
    return render(request, 'detail_list.html', context)


# def HomePageView(request):
#     news_list = News.published.all().order_by('-publish_time')[:1]
#     news_list_ = News.published.all().order_by('-publish_time')[1:7]
#     category = Category.objects.all()
#     local_news = News.published.all().filter(category__name='Mahalliy')
#     political_news = News.published.all().filter(category__name="Siyosat")
#     sport_news = News.published.all().filter(category__name='Sport')[:4]
#     last_modified = News.published.all().order_by('-upload_time')[:9]
#     context = {
#         'category': category,
#         'news_list': news_list,
#         'news_list_': news_list_,
#         'local_news': local_news,
#         'political_news': political_news,
#         'sport_news': sport_news,
#         'last_modified': last_modified
#     }
#     return render(request, 'index.html', context)
class HomePageView(ListView):
    template_name = 'index.html'
    model = News
    model=Category
    context_object_name = 'news'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=self.model.objects.all()
        context['news_list_']=News.published.all().order_by('-publish_time')[1:7]
        context['news_list']=News.published.all().order_by('-publish_time')[:1]
        context['local_news']=News.published.all().filter(category__name='Mahalliy')
        context['political_news']=News.published.all().filter(category__name="Siyosat")
        context['sport_news']=News.published.all().filter(category__name='Sport')[:4]
        context['last_modified']=News.published.all().order_by('-upload_time')[:9]
        return context


# def ContactView(request):
#     form=ContactForm(request.POST or None)
#     if request.method=='POST' and form.is_valid():
#         form.save()
#     context={
#         'form':form
#     }
#     return render(request,'Contact_us.html',context)


class ContactView(TemplateView):
    template_name = 'Contact_us.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'Contact_us.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse('Assalomu alaykum kebsiz kebisz')
        context = {
            'form': form
        }
        return render(request, 'Contact_us.html', context)
class LocalView(ListView):
    model = News
    template_name = 'local_news.html'
    context_object_name = 'Mahalliyhabarlar'
    def get_queryset(self):
        name=News.published.all().filter(category__name='Mahalliy')
        return name
class PoliticalView(ListView):
    model = News
    template_name = 'political_news.html'
    context_object_name = 'Siyosiyhabarlar'
    def get_queryset(self):
        name = News.published.all().filter(category__name='Siyosat')
        return name
class SportView(ListView):
    model = News
    template_name = 'sport_news.html'
    context_object_name = 'Sporthabarlari'
    def get_queryset(self):
        name=News.published.all().filter(category__name='Sport')
        return name
