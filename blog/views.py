from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from haystack.query import SearchQuerySet
from taggit.models import Tag

from .forms import EmailPostForm, CommentForm, SearchForm
from .models import Post, Comment
# Create your views here.

# this is home page
def home_page(request):
    return render(request, 'home.html')

def post_list(request, tag_slug=None):

    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 post each page
    # get the page number from request
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an interger deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if out of range deliver the last page
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {
                      'page': page,
                      'posts': posts,
                      'tag': tag
                  }
    )




def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                    .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                    .order_by('-same_tags', '-publish')[:4]

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(
                reverse('blog:post_detail',
                        args=[post.publish.year,
                              post.publish.strftime('%m'),
                              post.publish.strftime('%d'),
                              post.slug])
                )

    else:
        comment_form = CommentForm()

    return render(request,
                  'blog/post/detail.html',
                  {
                      'post': post,
                      'comments': comments,
                      'comment_form': comment_form,
                      'similar_posts': similar_posts,
                  })


def post_share(request, post_id):
    # retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    # if is submitted
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        # if not valid, you will see a bunch of errors
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = '{} ({}) recommends your reading "{}"'.\
                      format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.\
                      format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'ttloda@tom.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request,
                  'blog/post/share.html',
                  {
                      'post': post,
                      'form': form,
                      'sent': sent,
                  })


def post_search(request):
    form = SearchForm()
    cd = ''
    results = ''
    total_results = 0
    show_results = False
    # if is search
    if 'query' in request.GET:
        show_results = True
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Post)\
                      .filter(content=cd['query']).load_all()
            total_results = results.count()

    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'cd': cd,
                   'show_results': show_results,
                   'results': results,
                   'total_results': total_results,}
    )
