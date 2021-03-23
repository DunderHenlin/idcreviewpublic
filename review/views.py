from django.shortcuts import render, get_object_or_404,HttpResponse
from .models import Review
from .models import Profile

def home(request):
    profile=Profile.objects.all()[0]
    reviews=Review.objects.order_by('-releasedate')[:3]
    context={'reviews':reviews,'profile':profile}
    return render(request,"port/home.html",context)

def review(request):
    reviews= Review.objects.order_by('-releasedate')
    context={'reviews':reviews }
    return render(request,"port/blog.html",context)

def about(request):
    profile=Profile.objects.all()[0]
    context={'profile':profile}
    return render(request,"port/about.html",context)

def detail(request,review_id):
    review=get_object_or_404(Review,pk=review_id)
    context={'review': review}
    return render(request,'port/detail.html',context)

def search(request):
    query=request.GET['query']
    allReviewsTitle=Review.objects.filter(title__icontains=query)
    allReviewsDescription=Review.objects.filter(description__icontains=query)
    allReviews= allReviewsTitle.union(allReviewsDescription)
    context={'allReviews':allReviews, 'query':query}
    return render(request,"port/search.html",context)