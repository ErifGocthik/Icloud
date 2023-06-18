from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView, ListView

from cloud.forms import ImageForm, ArchiveForm
from cloud.models import Image, Archive


class CloudList(ListView):
    model = Image
    context_object_name = 'cloud'
    template_name = 'image_form.html'

    def post(self, request):
        if request.method == 'POST':
            form = ImageForm(data=request.POST,
                             files=request.FILES,)
            if form.is_valid():
                form.save()
                return redirect(reverse('main:img_form'))
        else:
            form = ImageForm()

        context = {'form': form}
        return render(request, 'image_form.html', context)

    def get(self, request):
        form = ImageForm
        context = {'form': form}
        return render(request, 'image_form.html', context)

class ArchiveListForm(ListView):
    model = Archive
    context_object_name = 'archive'
    template_name = 'root.html'

    def post(self, request):
        if request.method == 'POST':
            form = ArchiveForm(data=request.POST,
                               files=request.FILES,)
            if form.is_valid():
                form.save()
                return redirect(reverse('main:archive_form'))
        else:
            form = ArchiveForm()

        context = {'form_archives': form}
        return render(request, 'root.html', context)

    def get(self, request):
        form = ArchiveForm
        context = {'form_archives': form}
        return render(request, 'root.html', context)


class ArchiveList(ListView):
    model = Archive
    context_object_name = 'archives'
    template_name = 'archives.html'


class ArchiveList2(ListView):
    model = Archive
    context_object_name = 'archives_2'
    template_name = 'main_page.html'


class ArchiveCycle(ListView):
    model = Archive
    context_object_name = 'archive_cycle'
    template_name = 'archives_cycle.html'

class ArchiveDetails(DetailView):
    model = Archive
    context_object_name = 'archive_det'
    template_name = 'archive_detail.html'


# def cloud_list_view(request):
#     cloud = Image.objects.all()
#     context = {'clouds': cloud}
#     return render(request, 'main_page.html', context)

class CloudListMain(ListView):
    context_object_name = 'clouds'
    template_name = 'main_page.html'
    queryset = Image.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CloudListMain, self).get_context_data(**kwargs)
        context['archives'] = Archive.objects.all()
        return context

def cloud_image_detail(request, id):
    cloud_image = Image.objects.get(id=id)
    return render(request, 'image_detail.html', context={'images': cloud_image})


def test_view(request):
    test = Archive.objects.all()
    return render(request, 'test.html', context={'tests': test})


def delete_from_cloud(request, id):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        raise PermissionDenied
    image_del = Image.objects.get(id=id)
    try:
        image_del.delete()
    except KeyError as e:
        return JsonResponse({'successed': False})
    return JsonResponse({'successed': True})


def delete_from_archive(request, id, pk):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        raise PermissionDenied
    archive = Archive.objects.get(id=id)
    try:
        archive.images.remove(Image.objects.get(id=pk))
    except KeyError as e:
        return JsonResponse({'successed': False})
    return JsonResponse({'successed': True})

def add_image_in_archive(request, id, pk):
    # if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     raise PermissionDenied
    archive = Archive.objects.get(id=id)
    image = Image.objects.get(id=pk)
    try:
        archive.images.add(image)
    except KeyError as e:
        return JsonResponse({'successed': False})
    return JsonResponse({'successed': True})

def controlImageInArchive(request, id, pk):
    archive = Archive.objects.get(id=id)
    image = Image.objects.get(id=pk)
    if image not in archive.images.all():
        return JsonResponse({'ifResult': False})
    else:
        return JsonResponse({'ifResult': True})

def remove_image_from_archive(request, id, pk):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        raise PermissionDenied
    archive = Archive.objects.get(id=id)
    image = Image.objects.get(id=pk)
    try:
        archive.images.remove(image)
    except KeyError as e:
        return JsonResponse({'successed': False})
    return JsonResponse({'successed': True})