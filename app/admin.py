from django.contrib import admin
from .models import Category, Location, Business, Enquiry, Leads, Review,Advertisement,ZodiacDailyMessage,News,IyerProfile,PoojaService,PoojaBooking,BusinessBlog


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('reviewer', 'rating', 'comment', 'created_at')
    can_delete = False


class EnquiryInline(admin.TabularInline):
    model = Enquiry
    extra = 0
    readonly_fields = ('enquired_person', 'message', 'created_at', 'updated_at')
    can_delete = False


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'business_district', 'business_type', 'business_contact', 'active', 'premium', 'trusted', 'verified', 'views_count')
    list_filter = ('active', 'premium', 'trusted', 'verified', 'business_type', 'business_district')
    search_fields = ('business_name', 'business_contact', 'business_whatsapp', 'slug')  # <-- change here
    prepopulated_fields = {'slug': ('business_name',)}  # <-- change here
    readonly_fields = ('created_at', 'updated_at', 'views_count')
    inlines = [ReviewInline, EnquiryInline]



class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('enquired_person', 'enquired_business', 'created_at')
    search_fields = ('enquired_person__username', 'enquired_business__business_name')
    readonly_fields = ('created_at', 'updated_at')


class LeadsAdmin(admin.ModelAdmin):
    list_display = ('visited_person', 'visited_business', 'created_at')
    search_fields = ('visited_person__username', 'visited_business__business_name')
    readonly_fields = ('created_at',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'business', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('reviewer__username', 'business__business_name')
    readonly_fields = ('created_at',)
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Leads, LeadsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Advertisement)
admin.site.register(ZodiacDailyMessage)
admin.site.register(News)
admin.site.register(IyerProfile)
admin.site.register(PoojaService)
admin.site.register(PoojaBooking)
admin.site.register(BusinessBlog)