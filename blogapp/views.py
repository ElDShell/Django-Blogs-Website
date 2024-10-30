from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,DetailView,DeleteView,UpdateView,CreateView
from .models import Comment,Blog 
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count,Q
from taggit.models import Tag
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator 


# Blogs views 
class HomeView(TemplateView):
    
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        if search:
            blogs = Blog.objects.filter(Q(title__icontains=search)|Q(tags__name__icontains=search)).distinct()
            print(blogs)# test line
        else:
            blogs = Blog.objects.annotate(comments_num=Count('comments')).order_by('-id')
        
        pag = Paginator(blogs,2)
        page_number = self.request.GET.get('page')
        page_obj =pag.get_page(page_number)
                
        context["blogs"] =  page_obj
        return context

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = "create_blog.html"
    fields = ['title','image','content','tags']
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,"Blog has been created successfully")
        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.all()
        for comment in comments:
            comment.comment_delete_url = reverse('comment_delete',args=[comment.id])
        context["comments"] = comments
        context["form"] = CommentForm()
        context["blog"] = self.object
        return context
    
    def post(self,request,*args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            if self.request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.blog =self.object
                comment.author = request.user
                comment.content = request.POST.get('content')
                comment.active = True
                comment.save()
                return redirect(self.get_object().get_absolute_url())
            else:
                messages.warning(request,"Login First to write a comment")
                next_url = self.request.get_full_path()
                return redirect(f"/users/login?next={next_url}")
        return self.render_to_response({'form':form})
    
class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = "blog_edit.html"
    fields = ['image','title','content','tags']
    
class BlogImageUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    form_class = BlogImageForm
    template_name = None
    
    def get_success_url(self):
        blog = self.get_object()
        return reverse_lazy("blog_edit", args=[blog.id]) 
    
    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        
        if blog.image:
            blog.image.delete(save=False)
        blog.image = self.request.FILES.get("blog_image")
        blog.save()
        messages.success(self.request,f"{blog.title} Blog has been updated Successfully")
        return redirect(self.get_success_url())
    
class BlogTitleUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ['title']
    template_name = None
    
    def get_success_url(self):
        blog = self.get_object()
        messages.success(self.request,f"{blog.title} Blog has been updated Successfully")
        return reverse_lazy("blog_edit", args=[blog.id]) 

class BlogContentUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = None
    fields = ['content']
    def get_success_url(self):
        blog = self.get_object()
        messages.success(self.request,f"{blog.title} Blog has been updated Successfully")
        return reverse_lazy('blog_edit',args=[blog.id])

class BlogTagsUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = None
    fields=['tags']
    
    def get_success_url(self):
        blog = self.get_object()
        return reverse_lazy("blog_edit",args=[blog.id])
    def post(self, request, *args, **kwargs):
        action =  request.POST.get('action')
        blog = self.get_object()
        if action == "delete_tag":
            print(f"BLog:{blog.title}")       # test line     
            print("Yes It's Delete Tag")# test line
            tag_id = request.POST.get("tag_id")
            if tag_id:
                tag = Tag.objects.get(id=tag_id)
                tag.delete()
                print("Blog tag has been deleted")# test line
                messages.success(self.request,f"{blog.title} Blog has been updated Successfully")
            else:
                print("No tag ID provided")# test line
            blog.save()
        elif action =="add_tag":
            print(f"Action:{action}")# test line
            print("Yes It's Add Tag")# test line
            try:
                tag_name = request.POST.get("tag_name")
                if tag_name == "" :
                    messages.warning(request, "Please enter a tag name before adding.")
                    return redirect(self.get_success_url())
                print(f"Tag:{tag_name}")# test line
                blog.tags.add(tag_name)
                print(f"Tag '{tag_name}' added to blog '{blog.title}' successfully.")# test line
            except Blog.DoesNotExist:
                print("Blog not found.")# test line
        return redirect(self.get_success_url())

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = None
    
    def get_success_url(self):
        messages.warning(self.request,'Blog has been deleted')
        return reverse_lazy('home')
    def delete(self, request, *args, **kwargs):
        blog = self.get_object()
        return super().delete(request, *args, **kwargs)


class TagsView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('tag_slug')
        
        if tag_slug:
            context["blogs"] = Blog.objects.filter(tags__slug=tag_slug)
        else:
            context["blogs"] = Blog.objects.all()
        return context

#Comments views
class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = None
    
    def get_success_url(self):
        blog_id = self.get_object().blog.id
        return reverse_lazy('blog_detail',args=[blog_id]) 

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        return super().delete(request, *args, **kwargs)

#Extra Views
class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] =About.objects.first() 
        return context
    
class ContactView(TemplateView):
    template_name = "contact.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context
    
