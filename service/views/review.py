from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from service.models import Review


class ReviewListView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'service/review.html'
    model = Review
    fields = ('customer', 'review')
    success_url = reverse_lazy('service:review_list')
    context_object_name = 'reviews'
    # paginate_by = 5  # Number of reviews per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Include the form in the context
        return context

    def get_queryset(self):
        return Review.objects.all().order_by('-id')