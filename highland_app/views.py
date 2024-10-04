from django.shortcuts import render, redirect

# View for the index page
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def property(request):
    return render(request, 'property.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def propertydetail(request):
    return render(request, 'propertydetail.html')

# def loginpage(request):
#     return render(request, 'loginpage.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Check if the username and password are correct
#         if username == 'admin' and password == 'admin':
#             # Redirect to admin homepage
#             return redirect('admin_home')  # Replace with the actual URL name of your admin homepage
#         else:
#             # Handle incorrect credentials
#             return render(request, 'login.html', {'error': 'Invalid username or password'})

#     return render(request, 'login.html')

# def admin_home(request):
#     return render(request, 'admin_home.hml')