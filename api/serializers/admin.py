from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import House, HouseImage
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.hashers import make_password


class StaffMembersSerializer(serializers.ModelSerializer):
    password = password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        staff_member = super().create(validated_data)
        staff_member.is_staff = True
        staff_member.is_superuser = False
        staff_member.password = make_password(
            validated_data.get('password'))
        staff_member.save()
        return staff_member

    def update(self, instance, validated_data):
        validated_data.pop('password')
        return super().update(instance, validated_data)


class HouseImagesSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = Base64ImageField(allow_null=True)

    class Meta:
        model = HouseImage
        fields = ('id', 'image')


class GetHouseSerializer(serializers.ModelSerializer):
    images = HouseImagesSerializer(source='houseimage_set', many=True)

    class Meta:
        model = House
        fields = ('id', 'title', 'image', 'rooms', 'bathrooms', 'has_kitchen', 'has_AC',
                  'has_parking', 'has_wifi', 'has_tv', 'description', 'price', 'is_available', 'images')


class HouseImagesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = Base64ImageField(allow_null=True)

    class Meta:
        model = HouseImage
        fields = ('id', 'image')


class CreateUpdateHouseSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    images = HouseImagesSerializer(many=True)

    class Meta:
        model = House
        fields = ('id', 'title', 'image', 'rooms', 'bathrooms', 'has_kitchen', 'has_AC',
                  'has_parking', 'has_wifi', 'has_tv', 'description', 'price', 'is_available', 'images')

    def create(self, validated_data):
        images = validated_data.pop('images')
        house = super().create(validated_data)
        try:
            for image in images:
                for key, value in image.items():
                    HouseImage.objects.create(house_id=house, image=value)
        except:
            pass
        return house

    def update(self, instance, validated_data):
        print(validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.rooms = validated_data.get('rooms', instance.rooms)
        instance.bathrooms = validated_data.get(
            'bathrooms', instance.bathrooms)
        instance.has_kitchen = validated_data.get(
            'has_kitchen', instance.has_kitchen)
        instance.has_AC = validated_data.get('has_AC', instance.has_AC)
        instance.has_parking = validated_data.get(
            'has_parking', instance.has_parking)
        instance.has_wifi = validated_data.get('has_wifi', instance.has_wifi)
        instance.has_tv = validated_data.get('has_tv', instance.has_tv)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.price = validated_data.get('price', instance.price)

        images = validated_data.pop('images')
        # print(images)
        for image in images:
            print(image)
            house_image, created = HouseImage.objects.update_or_create(
                id=image.get('id'), house_id=instance)
            if image['image'] is not None and created:

                house_image.image = image['image']
                house_image.save()
            else:
                house_image.delete()

        instance.save()
        return instance
