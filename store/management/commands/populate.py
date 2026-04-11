from django.core.management.base import BaseCommand
from store.models import posts


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        post=[{"name":"Flared Maxi Dress","price":"₹200","img":"i1.jpg"}
,{"name":"Empire Pleat Kurti","price":"₹200","img":"i2.jpg"}
,{"name":"Lace Panel Kurta","price":"₹200","img":"i3.jpg"}
,{"name":"Urban Chic Kurti","price":"₹200","img":"i4.jpg"}
,{"name":"Fusion Style Kurti","price":"₹200","img":"i5.jpg"}
,{"name":"Regal Silk Kurti","price":"₹200","img":"i6.jpeg"}
,{"name":"Golden Glow Kurti","price":"₹200","img":"i7.jpeg"}
,{"name":"Breezy Wear Kurti","price":"₹200","img":"i8.jpeg"}
,{"name":"Graceful A-Line Kurti","price":"₹200","img":"i9.jpeg"}
,{"name":"Golden Glow Kurti","price":"₹200","img":"i10.jpeg"}
,{"name":"about1","price":"₹0","img":"about1.jpeg"}
,{"name":"about2","price":"₹0","img":"about2.jpeg"}
]
        for i in post:
            posts.objects.get_or_create(name=i["name"],price=i["price"],image="products/"+i["img"])

        self.stdout.write(self.style.SUCCESS("Products added successfully"))