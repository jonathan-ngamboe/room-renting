from rest_framework import serializers
from .models import  Booking, Property, PropertyType, Amenity, Status, Image, City, Review, Message, CustomUser, Unavailability
from django.db.models import Avg

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = CustomUser
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'groups', 'date_of_birth', 'date_joined', 'last_login', 'properties', 'profil_image', 'address', 'city']

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['url', 'id', 'check_in', 'check_out', 'created_at', 'status', 'property', 'user']

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'id', 'image_url', 'ext_url']

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['url', 'name', 'zip']

class AmenitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amenity
        fields = ['url', 'name']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    booking_id = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='booking.id'
    )
    booking = serializers.HyperlinkedRelatedField(
        view_name='booking-detail',
        queryset=Booking.objects.all(),
        write_only=True
    )
    user = CustomUserSerializer(read_only=True) 
    class Meta:
        model = Review
        fields = ['url', 'id', 'rating', 'comment', 'created_at', 'booking', 'booking_id', 'review_type', 'user']

class UnavailabilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unavailability
        fields = ['url', 'id', 'start_date', 'end_date', 'comment', 'property']

class PropertySerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), 
        source='city',  # Specifies that this field is to be used to update the 'city' field in the template
        write_only=True  # This field can only be used for writing, and will not be included in the API response.
    )
    city = CitySerializer(read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    amenities_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Amenity.objects.all(),
        source='amenities',
        write_only=True
    )
    images_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Image.objects.all(),
        source='images',
        write_only=True
    )
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = ['id', 'url', 'title', 'description', 'address', 'city', 'city_id', 'price_per_night', 'surface', 'is_active', 'created_at', 'updated_at', 'owner', 'images','images_ids','average_rating', 'amenities', 'amenities_ids', 'reviews', 'unavailabilities', 'bookings']

    def get_average_rating(self, obj):
        average = Review.objects.filter(
            booking__property=obj,  
            review_type='property'  
        ).aggregate(Avg('rating'))  

        return average['rating__avg'] if average['rating__avg'] is not None else 0


    def get_reviews(self, obj):
        reviews = Review.objects.filter(booking__property=obj)
        serializer = ReviewSerializer(reviews, many=True, context=self.context)
        return serializer.data


class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['url', 'name']

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['url', 'name']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['url', 'id', 'subject', 'body', 'sent_at', 'bookings']


