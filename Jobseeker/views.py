from django.shortcuts import render

# Create your views here.
def login_page(request):
     return render(request, "login.html")
  #  if request.method == "POST":
     #   email = request.POST.get('email')
      #  password = request.POST.get('password')
      #  if not User.objects.filter(email=email).exists():
       #     messages.error(request, "Email address not found!")
        #    return redirect('/login/')
        #try:
         #   user = User.objects.get(email=email)
         #   user = authenticate(request, username=user.username, password=password)
         #   if user is None:
          #      messages.error(request, "Invalid Password")
          #      return redirect('/login/')
          #  else:
          #      login(request, user)
          #      return redirect('/meetup/')
        #except:
         #   messages.error(request, "Email not found")
         #   return redirect('/login/')
   # return render(request, "login.html")
def registration(request):
    return render(request,"register.html")