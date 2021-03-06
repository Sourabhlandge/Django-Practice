from blog_app.models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from blog_app.forms import EmailSendForm,CommentForm


# Create your views here.
class Post_list_view(ListView):
    model = Post
    paginate_by = 2
    template_name = "blog/post_list.html"


class Post_detail_view(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    comments = Post.comments.filter(active=True)
    csubmit = False

def mail_send(request,post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you to read" f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\s comments: {cd['comments']}"
            send_mail(subject, message, 'sourabhlandge@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailSendForm()
    return render(request, 'blog/sharebymail.html', {'form':form,'post': post, 'sent': sent})
