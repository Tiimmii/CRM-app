from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class ManualLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organisor"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organisor:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

class AgentLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an agent"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_agent:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)