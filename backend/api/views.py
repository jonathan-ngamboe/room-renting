from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, permissions
from .models import  Booking, Property, PropertyType, Amenity, Status, Image, City, Review, Message, CustomUser, Unavailability
from .serializers import   BookingSerializer, PropertySerializer, PropertyTypeSerializer, AmenitySerializer, StatusSerializer, ImageSerializer, CitySerializer, ReviewSerializer, MessageSerializer, CustomUserSerializer, UnavailabilitySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from django.http import JsonResponse

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    """
    Retrieve the currently logged in user.
    """
    serializer = CustomUserSerializer(request.user, context={'request': request})
    return Response(serializer.data)

def send_confirmation_email(request):
    email = request.POST.get('email', '')
    room_title = request.POST.get('roomTitle', '')
    check_in = request.POST.get('checkIn', '')
    check_out = request.POST.get('checkOut', '')
    total_price = request.POST.get('totalPrice', '')

    subject = 'Booking Confirmation'
    message = f'Your booking for {room_title} has been confirmed. Check-in: {check_in}, Check-out: {check_out}, Total Price: {total_price}'
    sender = None # Django will use the value of the DEFAULT_FROM_EMAIL setting
    recipients = [email]

    try:
        send_mail(subject, message, sender, recipients, fail_silently=False)
        return JsonResponse({'status': 'success', 'message': 'Confirmation email sent successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows custom users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict non-staff users to only access their own user object
        if self.request.user.is_staff:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=self.request.user.id)

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows properties to be viewed or edited.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]

class PropertyTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows property types to be viewed or edited.
    """
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class AmenityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows amenities to be viewed or edited.
    """
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [permissions.IsAuthenticated]

class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows statuses to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

class UnavailabilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows unavailabilities to be viewed or edited.
    """
    queryset = Unavailability.objects.all()
    serializer_class = UnavailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]
    
# def add_property_view(request):
#    if request.method == 'POST':
#        property_data = request.POST  
#        try:
#            new_property = propertyService.addProperty(property_data)
#            return JsonResponse({'success': True, 'message': 'Property added successfully', 'property': new_property})
#        except Exception as e:
#            return JsonResponse({'success': False, 'error': str(e)})
#    else:
#        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed for this endpoint'}, status=405)
