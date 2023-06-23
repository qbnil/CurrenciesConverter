# # middleware.py
# from django.shortcuts import redirect
# from django.urls import reverse

# class AuthMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
        
#     def __call__(self, request):
#         print('AuthMiddleware: request.path =', request.path)
        
#         if not request.user.is_authenticated: # check if user is authenticated
#             print('AuthMiddleware: User is not authenticated, redirecting to registration page')
#             return redirect(reverse('register')) # Redirect to the named URL pattern for the registration page
        
#         # check if user has access to the exchange_app
#         if request.path.startswith('/main'):
#             if not request.user.is_registered: # assuming you have a custom is_registered field in your User model
#                 print('AuthMiddleware: User is not registered, redirecting to registration page')
#                 return redirect(reverse('register'))

#         response = self.get_response(request)
#         return response
