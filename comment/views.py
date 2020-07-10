from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View
from django.template.loader import render_to_string
from .models import Comment
from .forms import CommentForm


# display all comments 
class CommentList(ListView):
    model = Comment
    template_name = 'comment/comment_list.html'
    context_object_name = 'comment_list'



'''
================ comment_create view ================

  notice that 2 partial templates has been created:
  - partail_comment_create.html: display a CommentForm
  - partail_comment_list.html: display comment_list 

  when get request:
    retreive partail_comment_create.html and display the form for the user
  when post request:
    if form is valide
      save form
      return partail_comment_list.html
    if form is not valide
      rerender partail_comment_create.html and display the form for the user with errors
'''

class CommentCreate(View):
    data = dict()

    def get(self, request): # render partial_comment_create.html for user
        data = self.data
        form = CommentForm()
        data['html_form'] = render_to_string('comment/partial_comment_create.html', {'form': form}, request=request)
        return JsonResponse(data)

    def post(self, request): # validate form and render partial_comment_list.html if success
        data = self.data
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['html_comment_list'] = render_to_string('comment/partial_comment_list.html', 
                    {'comment_list': Comment.objects.all()}, 
                    request=request)
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['html_form'] = render_to_string('comment/partial_comment_create.html', {'form': form}, request=request)
            return JsonResponse(data)

class CommentUpdate(View):
    data = dict()

    def get(self, request, *args, **kwargs): # render partial_comment_udpate.html for user
        data = self.data
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        print(comment)
        form = CommentForm(instance=comment)
        data['html_form'] = render_to_string('comment/partial_comment_update.html', {'form': form}, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs): # validate form and render partial_comment_list.html if success
        data = self.data
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['html_comment_list'] = render_to_string('comment/partial_comment_list.html', 
                    {'comment_list': Comment.objects.all()}, 
                    request=request)
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['html_form'] = render_to_string('comment/partial_comment_update.html', {'form': form}, request=request)
            return JsonResponse(data)



class CommentDelete(View):
    data = dict()

    def post(self, request, *args, **kwargs): # delete comment and render partial_comment_list.html if success
        data = self.data
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        comment.delete()
        data['html_comment_list'] = render_to_string('comment/partial_comment_list.html', 
                {'comment_list': Comment.objects.all()}, 
                request=request)
        return JsonResponse(data)

    def get(self, request, *args, **kwargs): # render partial_comment_delete.html for user
        data = self.data
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        data['html_form'] = render_to_string('comment/partial_comment_delete.html', {'comment': comment}, request=request)
        return JsonResponse(data)


