from django.shortcuts import render, get_object_or_404
from . models import Category,Business,Review,Advertisement,Location,ZodiacDailyMessage , News,IyerProfile,BusinessBlog
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import ReviewForm  # you will create a simple form
from django.template.loader import render_to_string
from django.db.models import Avg
from django.views.decorators.http import require_POST
from datetime import date

    
'''
For home page
'''
def index(request):
    categories = Category.objects.filter(parent__isnull=True)
    advertisement = Advertisement.objects.all()
    location = Location.objects.all()
    news = News.objects.all()
    businessblog = BusinessBlog.objects.all()
    trending = Business.objects.all().order_by('-views_count')[:15]

    # Get today's message or latest available if today doesn't exist
    try:
        zodiac_message = ZodiacDailyMessage.objects.get(date=date.today())
    except ZodiacDailyMessage.DoesNotExist:
        zodiac_message = None

    return render(
        request,
        'app/pages/index.html',
        {
            'categories': categories,
            'advertisement': advertisement,
            'location': location,
            'zodiac_message': zodiac_message,
            'news':news,
            'businessblog':businessblog,
            'trending':trending
        }
    )

def about(request):
    return render(request,'app/pages/about.html')

def contact(request):
    return render(request,'app/pages/contact.html')



'''
for business detail
'''
def business_detail(request,slug):
    form = ReviewForm()
    business = Business.objects.get(slug=slug)
    business.views_count += 1
    business.save()

    reviews = business.reviews.all()[:5]
    total_reviews = business.reviews.count()
    average_rating = business.reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    return render(request,'app/pages/business_detail.html',{
        'business':business,
        'form':form,
        'reviews':reviews,
        'total_reviews': total_reviews,
        'average_rating': round(average_rating,1),
    })


from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Business, Category, Location

def category_detail(request, **kwargs):
    location = kwargs.get('location')
    slug = kwargs.get('slug')
    parent_slug = kwargs.get('parent_slug')
    grandparent_slug = kwargs.get('grandparent_slug')
    all_locations = Location.objects.all()
    location_id = get_object_or_404(Location, slug=location)

    # Determine category
    if grandparent_slug:
        category = Category.objects.filter(
            slug=slug,
            parent__slug=parent_slug,
            parent__parent__slug=grandparent_slug
        ).first()
        catitle = grandparent_slug
    elif parent_slug:
        category = Category.objects.filter(
            slug=slug,
            parent__slug=parent_slug
        ).first()
        catitle = parent_slug
    else:
        category = Category.objects.filter(
            slug=slug,
            parent=None
        ).first()
        catitle = slug

    subcategories = category.get_subcategories()

    if not subcategories:
        businesses = Business.objects.filter(
            business_type=category,
            business_district=location_id,
            active =True
        )

        # Annotate with average rating from related reviews
        businesses = businesses.annotate(avg_rating=Avg('reviews__rating'))

        # Filter type (trusted, premium, etc.)
        filter_type = request.GET.get('filter')
        if filter_type == "premium":
            businesses = businesses.filter(premium=True)
        elif filter_type == "verified":
            businesses = businesses.filter(verified=True)
        elif filter_type == "trusted":
            businesses = businesses.filter(trusted=True)
        elif filter_type == "most_viewed":
            businesses = businesses.order_by('-views_count')
        elif filter_type == "top_ranked":
            businesses = businesses.filter(is_top_in_category=True).order_by('top_rank')

        # Avg Rating filter (1 to 5 stars)
        avg_rating = request.GET.get('avgRating')
        if avg_rating and avg_rating.isdigit():
            businesses = businesses.filter(avg_rating__gte=int(avg_rating))

        # Pagination
        paginator = Paginator(businesses, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'app/pages/business_list.html', {
            'page_obj': page_obj,
            'catitle': catitle,
            'all_locations': all_locations,
            'filter_type': filter_type,
        })

    else:
        return render(request, 'app/pages/categories.html', {
            'category': category,
            'subcategories': subcategories,
            'catitle': catitle,
            'location': location
        })

'''
business reviews
'''
def business_reviews(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    reviews = business.reviews.all()[:5]  # First 5 reviews
    total_reviews = business.reviews.count()
    average_rating = business.reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    form = ReviewForm()

    return render(request, 'reviews/business_reviews.html', {
        'business': business,
        'reviews': reviews,
        'total_reviews': total_reviews,
        'average_rating': round(average_rating, 1),
        'form': form,
    })


'''
loading more reviews
'''
def load_more_reviews(request, business_id):
    offset = int(request.GET.get('offset', 0))
    limit = 5
    business = get_object_or_404(Business, id=business_id)
    reviews = business.reviews.all()[offset:offset+limit]
    data = []
    for review in reviews:
        data.append({
            'reviewer': review.reviewer.username,
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at.strftime("%b %d, %Y"),
        })
    return JsonResponse({'reviews': data})


'''
Adding review
'''
@require_POST
def add_review(request, business_id):
    business = get_object_or_404(Business, id=business_id)

    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.business = business
        review.reviewer = request.user
        review.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors})


'''
search functionality
'''
def search_business(request):
    query = request.GET.get('q', '')
    if query:
        businesses = Business.objects.filter(business_name__icontains=query)[:5]
    else:
        businesses = Business.objects.none()

    html = render_to_string('app/pages/search_results.html', {'businesses': businesses})
    return JsonResponse({'html': html})

import json
from django.contrib.auth.decorators import login_required
from .models import Enquiry

@login_required
def submit_enquiry(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        business_id = data.get('business_id')

        if not message:
            return JsonResponse({'status': 'error', 'error': 'Message cannot be empty'}, status=400)

        try:
            business = Business.objects.get(id=business_id)
        except Business.DoesNotExist:
            return JsonResponse({'status': 'error', 'error': 'Business not found'}, status=404)

        enquiry = Enquiry.objects.create(
            enquired_business=business,
            message=message,
            enquired_person=request.user
        )
        return JsonResponse({'status': 'success'})
    
def iyer_list(request):
    profiles = IyerProfile.objects.all().order_by('-id')
    paginator = Paginator(profiles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'app/pages/iyer_list.html',{
            'page_obj': page_obj,
            'catitle': 'iyers booking',
        })

def iyer_detail(request, id):
    profile = IyerProfile.objects.get(pk=id)
    bookings = PoojaBooking.objects.filter(user=request.user.id, iyer=profile)
    user_bookings = {booking.pooja.id: booking for booking in bookings}

    return render(request, 'app/pages/iyer_detail.html', {
        'profile': profile,
        'user_bookings': user_bookings,
    })


# views.py
from .models import IyerProfile, PoojaService, PoojaBooking
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required
def book_pooja(request, iyer_id, pooja_id):
    if request.method == 'POST':
        pooja_date = request.POST.get('pooja_date')
        iyer = get_object_or_404(IyerProfile, pk=iyer_id)
        pooja = get_object_or_404(PoojaService, pk=pooja_id)

        existing_booking = PoojaBooking.objects.filter(user=request.user, iyer=iyer, pooja=pooja).last()
        if existing_booking:
            messages.error(request, "You have already booked this pooja.")
            return redirect('iyer_detail', id=iyer.id)

        PoojaBooking.objects.create(
            user=request.user,
            iyer=iyer,
            pooja=pooja,
            pooja_date=pooja_date,
            status='pending'
        )
        profile = IyerProfile.objects.get(pk=iyer.id)
        bookings = PoojaBooking.objects.filter(user=request.user, iyer=profile)
        user_bookings = {booking.pooja.id: booking for booking in bookings}
        print(user_bookings)
        return render(request, 'app/pages/iyer_detail.html', {
            'profile': profile,
            'user_bookings': user_bookings,
        })


@login_required
def iyer_bookings(request):
    iyer = request.user.iyerprofile
    bookings = PoojaBooking.objects.filter(iyer=iyer, status='pending')
    return render(request, 'app/pages/iyer_bookings.html', {'bookings': bookings})

@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(PoojaBooking, pk=booking_id, iyer=request.user.iyerprofile)
    booking.status = 'confirmed'
    booking.save()
    messages.success(request, "Booking confirmed. User can now pay.")
    return redirect('index')


import razorpay
from django.conf import settings

@login_required
def start_payment(request, booking_id):
    booking = get_object_or_404(PoojaBooking, pk=booking_id, user=request.user, status='confirmed')
    client = razorpay.Client(auth=('rzp_test_lrSbqEXKLDzZCp', 'osxl3AkRenY743r7pS9hqQm1'))

    amount = int(booking.pooja.price * 100)  # in paisa
    price = booking.pooja.price

    payment = client.order.create({
        "amount": amount,
     
        "currency": "INR",
        "payment_capture": "1"
    })

    return render(request, 'app/pages/payment_page.html', {
        'booking': booking,
           "price":price,
        'order_id': payment['id'],
        'razorpay_key_id': 'rzp_test_lrSbqEXKLDzZCp',
        'amount': amount
    })

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import razorpay
import json

@csrf_exempt
@login_required
def payment_success(request):
    if request.method == "POST":
        data = json.loads(request.body)

        payment_id = data.get("razorpay_payment_id")
        order_id = data.get("razorpay_order_id")
        signature = data.get("razorpay_signature")
        booking_id = data.get("booking_id")

        client = razorpay.Client(auth=("rzp_test_lrSbqEXKLDzZCp", "osxl3AkRenY743r7pS9hqQm1"))

        try:
            # Verify the payment signature
            client.utility.verify_payment_signature({
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature
            })

            # Update booking
            booking = PoojaBooking.objects.get(id=booking_id, user=request.user)
            booking.status = "paid"
            booking.razorpay_payment_id = payment_id
            booking.save()

            return JsonResponse({"status": "success"})

        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({"status": "failure", "message": "Invalid signature"}, status=400)

    return JsonResponse({"status": "failure", "message": "Invalid request"}, status=400)


def business_blog(request,slug):
    blog = BusinessBlog.objects.get(slug=slug)
    return render(request,'app/pages/business_blog.html',{'blog':blog})