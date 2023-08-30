from .models import News
from .models import Category
def context_processor(request):
    category=Category.objects.all()
    latest_news = News.published.order_by('-publish_time')
    local_news = News.published.all().filter(category__name='Mahalliy')
    political_news = News.published.all().filter(category__name="Siyosat")
    sport_news = News.published.all().filter(category__name='Sport')[:4]
    last_modified = News.published.all().order_by('-upload_time')[:9]
    news_list = News.published.all().order_by('-publish_time')[:1]
    news_list_ = News.published.all().order_by('-publish_time')[1:7]
    context = {
        'latest_news': latest_news,
        'local_news':local_news,
        'political_news':political_news,
        'sport_news':sport_news,
        'last_modified':last_modified,
        'news_list':news_list,
        'news_list_':news_list_,
        'category':category
    }
    return context