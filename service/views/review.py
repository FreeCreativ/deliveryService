from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

from service.models import Review


class ReviewListView(LoginRequiredMixin, TemplateView):
    template_name = 'service/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        customer_name = request.POST.get('customer_name')
        review_content = request.POST.get('review')
        Review.objects.create(
            customer_name=customer_name,
            review=review_content,
        )
        return redirect('review_list')
