from django.shortcuts import render, redirect, get_object_or_404
from . models import SiteConfig
from django.contrib import messages
from . models import *
from . forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def index(request):
    partners = Partners.objects.order_by('-id')
    services = Services.objects.order_by('-id')
    return render(request, 'main/index.html', {'partners': partners, 'services': services})

def objects_map(request):
    return render(request, 'main/objects_map.html')

def portfolio(request):
    portfolio = Portfolio.objects.order_by('-id')[:10]
    return render(request, 'main/portfolio.html', {'portfolio': portfolio})

def about(request):
    partners = Partners.objects.order_by('-id')[:5]
    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
            subject = 'Заявка со страницы - О нас'
            user_name = form.cleaned_data['user_name']
            user_phone = form.cleaned_data['user_phone']
            message = form.cleaned_data['message']
            result = f'Имя: {user_name}, Телефон: {user_phone}, Сообщение: {message}'
            try:
                send_mail(subject, result, DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            context = {
                'success': 'Заявка отправлена.',
                'partners': partners,
                'form': form
            }
            return render(request, 'main/about.html', context)
        else:
            return HttpResponse('Ошибка валидации.')
    else:
        form = FeedBack()
        return render(request, 'main/about.html', {'partners': partners, 'form': form})

def blog(request):
    if request.method == 'POST':
        form = Sendpost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успешно отправлен на модерацию')
        else:
            messages.error(request, form.errors)
        return redirect('blog')
    else:
        search_query = request.GET.get('search', '')

        if search_query:
            if len(search_query) < 3:

                messages.error(request, 'Ошибка! Значение для поиска должно быть хотя бы 3 символа!')
                return redirect('blog')

            posts = Blog.objects.filter(
                Q(title__icontains=search_query) |
                Q(text__icontains=search_query),
                status='public'
            ).order_by('-id')

        else:
            posts = Blog.objects.filter(status='public').order_by('-id')

        form = Sendpost()

        paginator = Paginator(posts, 105)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'form': form,
            'search_query': search_query,
            'page_obj': page_obj
        }
        return render(request, 'main/blog.html', context)

def contacts(request):
    if request.method == 'POST':
        form = ContanctForm(request.POST)
        if form.is_valid():
            subject = 'Заявка со страницы - Контакты'
            user_name = form.cleaned_data['user_name']
            user_phone = form.cleaned_data['user_phone']
            user_email = form.cleaned_data['user_email']
            result = f'Имя: {user_name}, Телефон: {user_phone}, E-mail: {user_email}'
            try:
                send_mail(subject, result, DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            context = {
                'success': 'Заявка отправлена.',
                'form': form
            }
            return render(request, 'main/contacts.html', context)
        else:
            return HttpResponse('Ошибка валидации.')
    else:
        form = ContanctForm()
        return render(request, 'main/contacts.html', {'form': form})

def post(request, slug):
    post = get_object_or_404(Blog, slug=slug)

    comments = Comments.objects.filter(post=post, status='public')
    comments_form = CommentsForm()

    data = {
        'post': post,
        'comments': comments,
        'comments_form': comments_form
    }
    return render(request, 'main/post.html', data)

def add_comment(request, slug):
    if request.POST:
        form = CommentsForm(request.POST)
        post = get_object_or_404(Blog, slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Комментарий будет опубликован после модерации')
        else:
            messages.error(request, f"Комментарий не добавлен! {form.errors}")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def portfolio_single(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'main/portfolio_single.html', {'portf': portfolio})
