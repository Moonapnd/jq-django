from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Comment
from .forms import CommentForm

# display all comments 
def comment_list(request):
    comment_list = Comment.objects.all()
    context = {'comment_list': comment_list}
    return render(request, 'comment/comment_list.html', context)


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

def comment_create(request):
    data = dict()

    if request.method == 'POST':
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

    else:

        form = CommentForm()
        data['html_form'] = render_to_string('comment/partial_comment_create.html', {'form': form}, request=request)
        return JsonResponse(data)


def comment_update(request, pk):
    data = dict()

    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
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

    else:
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(instance=comment)
        data['html_form'] = render_to_string('comment/partial_comment_update.html', {'form': form}, request=request)
        return JsonResponse(data)

def comment_delete(request, pk):
    data = dict()

    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        data['html_comment_list'] = render_to_string('comment/partial_comment_list.html', 
                                                    {'comment_list': Comment.objects.all()}, 
                                                    request=request)
        return JsonResponse(data)

    else:
        comment = get_object_or_404(Comment, pk=pk)
        data['html_form'] = render_to_string('comment/partial_comment_delete.html', {'comment': comment}, request=request)
        return JsonResponse(data)


