from datetime import datetime, date


class OrderByMixin:
    def get_queryset(self):
        queryset = super().get_queryset()

        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset


class SearchMixin:
    """
        Usage:
            Set the attribute `filters` in your ListView with a list of tuples containing the
            parameter name comming from request, the filter argument to be used in model
            filtering and the value type.

        Sample:
            filters = (
                ('date_start', 'date_start', date),
                ('date_end', 'date_end', date),
                ('title', 'title__icontains', str),
            )
    """

    def get_queryset(self):
        queryset = super().get_queryset()

        if not hasattr(self, 'filters'):
            return queryset

        for request_param, model_filter_arg, type_ in self.filters:
            filter_value = self.request.GET.get(request_param)
            if filter_value:

                if type_ == date:
                    filter_value = datetime.strptime(filter_value, "%d/%m/%Y")
                elif type_ == bool:
                    if not filter_value == 'on':
                        continue
                    filter_value = True
                else:
                    filter_value = type_(filter_value)

                arguments = {model_filter_arg: filter_value}
                queryset = queryset.filter(**arguments)

        return queryset
