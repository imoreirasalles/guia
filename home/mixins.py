class OrderByMixin:
    def get_queryset(self):
        queryset = super().get_queryset()

        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset