from django.contrib import admin

from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('date_of_publication', 'description', 'pets')

    @staticmethod
    def pets(current_photo_obj):
        tagged_pets = [p.name for p in current_photo_obj.tagged_pet.all()]
        if tagged_pets:
            return ', '.join(tagged_pets)
        return 'No Pets'
