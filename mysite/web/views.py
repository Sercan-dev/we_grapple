
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import cache_page



from .models import Post, LastUpdate, Photo
from .forms import RegisterForm, LoginForm, PostForm


def index(request):
    return render(request, 'web/base.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('webpage:timeline', kwargs={'username': request.user.username}))
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('webpage:timeline', kwargs={'username': request.user.username}))
    return render(request, 'web/register.html', {'register_form': register_form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('webpage:timeline', kwargs={'username': request.user.username}))
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('webpage:timeline', kwargs={'username': request.user.username}))
    return render(request, 'web/login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect(reverse('web:index'))


def rules_view(request):
    return render(request, 'web/rules.html')


def gallery_view(request):
    queryset = Photo.objects.all()
    context = {
        'web': queryset,
    }
    return render(request, 'web/gallery.html', context)


@cache_page(None)
def home(request):
    """
    This is the public view that displays only published posts.
    The view also returns a UNIX timestamp of the most recently updated post.
    """

    posts = Post.objects.filter(published=True)
    latest = 0
    if posts:
        latest = Post.objects.latest('updated').unix_time()

    return render(request, 'web/base.html', {'posts': posts, 'latest': latest})


@login_required
def all(request):
    """
    This is a view for staff members that shows all posts, published or unpublished
    Each Post has a link that displays the Post and presents the option to publish or unpublish the post
    """

    posts = Post.objects.filter()

    print("made a query")
    return render(request, 'web/all.html', {'posts': posts})


@login_required
def toggle_publish(request, id):
    """
    This view allows an authenticated staff user to publish or unpublish an article by clicking a button.
    Clicking the button toggles the current state of the selected Post's `published` field.
    It also updates the `LastUpdated` time to be the time when the Post was updated (saved), tracked by its `updated` field
    This field uses `auto_now=True`, which updates the datetime field to the time at which the record is saved.
    Finally, the button triggers the clearing of the cache.
    This removes the cached home page and forces it to be refreshed with the published (or unpublished post).
    """

    instance = get_object_or_404(Post, id=id)

    if request.method == "POST":
        instance.published = not instance.published
        instance.save()

        t, created = LastUpdate.objects.get_or_create(id=1)

        t.updated = instance.updated
        t.save()

        cache.clear()
        return redirect('web:index')

    context = {'post': instance}

    return render(request, 'web/publish.html', context)


@login_required
def new(request):
    """
    This form allows for a staff user to create a new post.
    It does not publish the post, but it redirects to a page where the post can be reviewed and published.
    """

    form = PostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('web:toggle_publish', args=(instance.id,)))

    context = {'form': form}

    return render(request, 'web/new.html', context)


