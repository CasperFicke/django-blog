from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CommentForm

# Create your views here.

#def home(request):
#  return render(request, 'home.html', {})

class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  # ordering = ['-id']
  ordering = ['-post_date']
  # function to make data usable in html
  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context["cat_menu"] = cat_menu
    return context

#########
# POSTS #
#########

# show post
class PostView(DetailView):
  model = Post
  template_name = 'show_post.html'

  # function to make data usable in html
  def get_context_data(self, *args, **kwargs):
    # categorien menu tbv dropdown
    cat_menu = Category.objects.all()
    context = super(PostView, self).get_context_data(*args, **kwargs)
    
    # total likes
    stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    total_likes = stuff.total_likes()
    
    # liked status
    liked=False
    if stuff.likes.filter(id=self.request.user.id).exists():
      liked = True
    
    context["cat_menu"] = cat_menu
    context["total_likes"] = total_likes
    context["liked"] = liked
    return context


# add post
class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'add_post.html'
  # fields = '__all__'
  # fields = ('title', 'body')


# update post
class UpdatePostView(UpdateView):
  model = Post
  form_class = UpdateForm
  template_name = 'update_post.html'
  # fields = ['title', 'title_tag', 'body']

# delete post
class DeletePostView(DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')

##############
# CATEGORIES #
##############

# show all categories (functionbased view)
def CategoryView(request, cats):
  category_posts = Post.objects.filter(category=cats.replace('-', ' '))
  return render(
    request,
    'categories.html',
    {'cats':cats.title().replace('-', ' '),
    'category_posts': category_posts}
  )

# show all categories (functionbased view)
def CategoryListView(request):
  cat_list = Category.objects.all()
  return render(request, 'category_list.html', {'cat_list':cat_list})


# add category
class AddCategoryView(CreateView):
  model = Category
  # form_class = PostForm
  template_name = 'add_category.html'
  fields = '__all__'

# like post
def LikeView(request, pk):
  post = get_object_or_404(Post, id=request.POST.get('post_id'))
  liked = False
  if post.likes.filter(id=request.user.id).exists():
    post.likes.remove(request.user)
    liked = False
  else:
    post.likes.add(request.user)
    liked = True
  return HttpResponseRedirect(reverse('post-view', args=[str(pk)]))

############
# COMMENTS #
############

# add comment
class AddCommentView(CreateView):
  model = Comment
  form_class = CommentForm
  template_name = 'add_comment.html'
  # fields = '__all__'
  # success_url = reverse_lazy('home')
  # redirect to blogpost
  def get_success_url(self):
     return reverse_lazy('post-view', kwargs={'pk': self.kwargs['pk']})
  # function to get userid of loggendin user and use it to save profilepage
  def form_valid(self, form):
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)
