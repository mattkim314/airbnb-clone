from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets=(
        (
            "Basic Info",{
                "fields": (
                    "name", "description", "country", "address", "price"
                )
            }
        ),
        (
            "Times",{
                "fields":(
                    "check_in","check_out","instant_book"
                )
            }
        ),
        (
            "Space",{
                "fields": (
                    "guests", "beds", "bedrooms", "baths"
                )
            }
        ),
        (
            "More About the Space",{
                "classes":("collapse",),
                "fields":(
                    "amenities","facilities","house_rules"
                )
            }
        ),
        (
            "Last Detials",{
                "fields":(
                    "host",
                )
            }
        ),


    )


    list_display = (
        "name",
        "country",
        "city",
        "price",
        "beds",
        "bedrooms",
        "baths",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__gender",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
        "city",
    )
    search_fields = ('city',)

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules"
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    @admin.register(models.Photo)
    class PhotoAdmin(admin.ModelAdmin):

        """ Photo Admin Definition """

        pass
