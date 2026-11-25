from django.shortcuts import redirect, render


def home(request):
    if not request.session.get("age_verified"):
        error_message = ""
        if request.method == "POST":
            try:
                age = int(request.POST.get("age", ""))
            except ValueError:
                age = 0

            if age >= 18:
                request.session["age_verified"] = True
                request.session["show_age_welcome"] = True
                return redirect("home")
            error_message = "You must be 18 or older to enter this website."

        return render(request, "myapp/age_gate.html", {"error_message": error_message})

    show_welcome = request.session.pop("show_age_welcome", False)
    return render(request, "myapp/home.html", {"show_welcome": show_welcome})


def about(request):
    if not request.session.get("age_verified"):
        return redirect("home")
    return render(request, "myapp/about.html")


def contact(request):
    if not request.session.get("age_verified"):
        return redirect("home")
    return render(request, "myapp/contact.html")
