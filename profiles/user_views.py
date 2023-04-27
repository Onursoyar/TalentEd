from django.shortcuts import render
from django.views import View


class UserProfile(View):
    """Get user profile"""

    def get(self, request):
        return render(request, 'profile.html')
