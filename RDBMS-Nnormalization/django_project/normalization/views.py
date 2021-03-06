from django.views import generic
from .models import Order_details


class IndexView(generic.ListView):
    model = Order_details

    def get_queryset(self):
        result = self.model.objects.all()
        order_id = self.request.GET.get('order_id')
        if order_id != '' and isinstance(order_id, str) == True:
            result = self.model.objects.filter(order=order_id)

        return result
