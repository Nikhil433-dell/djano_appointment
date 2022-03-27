import datetime
from email import message
from django.views.generic import UpdateView
from django.http import HttpResponse
from user.models import Appointment, Blog, Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from user.Google import Create_Service
# Create your views here.

def home(request, id):
    profile = Profile.objects.get(id=id)
    blog = Blog.objects.filter(draft=False)
    return render(request, "home.html", {"profile": profile, "blog": blog})




def index(request):
    try:
        if request.method=="POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            type = request.POST.get('atype')

        # check if user has entered correct credentials
            user_obj = User.objects.get(email=email.lower())
            user = authenticate(username=user_obj, password=password)

            profile = Profile.objects.get(user=user_obj)
            if user is not None:
                login(request, user)
                return redirect(f"/home/{profile.id}")
            else:
                messages.error(request, "Wrong Password!")
                print('failed')
                return redirect("/")
    except Exception as e:
        print(e)
    return render(request, "index.html")



def sign_up(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            last_name = request.POST.get('lname')
            first_name = request.POST.get('fname')
            email = request.POST.get('email')
            password = request.POST.get('pass1')
            password2 = request.POST.get('pass2')
            address = request.POST.get('address')
            image = request.FILES.get('image')
            types = request.POST.get('atype')

            if password != password2:
                messages.error(request, "Error: Passwords not matching!")
                print("Passwords not matching!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Error: Email Taken!")
                print("Email Taken!")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Error: Username Taken!")
                print("Username Taken!")
            elif password == username:
                messages.error(request, "Password is not Strong!")
                print("Error: Password is not Strong!")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()

                profile = Profile(address=address, user=user, type=types, photo=image)
                profile.save()

                print("user_created")
                return redirect(f"/home/{profile.id}")
    except Exception as e:
        print(e)
        message.error("Account not created")

    return render(request, "sign_up.html")




def user_details(request, id):
    user = Profile.objects.get(id=id)

    context = {"user": user}
    return render(request, "user_details.html", context)



def logout(request):
    try:
        logout(request)
        print(f"{request.user}__logged out")
    except Exception as e:
        print(e)
    return redirect("/")


def create_blog(request, id):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        category = request.POST.get("category")
        summary = request.POST.get("summary")
        content = request.POST.get("content")
        draft = request.POST.get("draft")
        if draft == "on":
            draft = True
        else:
            draft = False

        blog = Blog.objects.create(title=title, image=image, category=category, summary=summary, content=content, draft=draft)
        blog.save()
        return redirect(f"/home/{id}")
    return render(request, "create_blog.html", {"id": id})





def drafted_blog(request, id):

    profile = Profile.objects.get(id=id)
    blog = Blog.objects.filter(draft=True)
    return render(request, "drafted_blog.html", {"profile": profile, "blog": blog})


def blog_details(request, id):

    blog = Blog.objects.filter(id=id).first()

    return render(request, "blog_details.html", {"blog": blog})




def doctors(request, id):

    avdoc = Profile.objects.filter(type="Doctor")
    profile = Profile.objects.get(id=id)

    return render(request, "doctors.html", {"avdoc": avdoc, "profile": profile})



def bookap(request, id):
    doc = Profile.objects.get(id=id)
    doctor_name = doc.user.username
    if request.method == "POST":
        speciality = request.POST.get('speciality')
        dateap = request.POST.get('dateap')

        start_time = request.POST.get('start_time')
        start_time = datetime.datetime.strptime(start_time, "%H:%M")

        end_time = start_time + datetime.timedelta(minutes=45)

        start_time = str(start_time)
        start_time = start_time.replace("1900-01-01", "")
        print(end_time.hour)

        # the datetime object can't return only time and it has to return some date with the start_time and end_time 

        if end_time.hour == 0:
            # replaing the defaullt date with blank
            end_time = str(end_time)

            # if end time goes to next day
            end_time = end_time.replace("1900-01-02", "")

        else:
            # replaing the defaullt date with blank
            end_time = str(end_time)

            # if end time is on same day
            end_time = end_time.replace("1900-01-01", "")

        
        appointment = Appointment.objects.create(doctor_name=doctor_name, speciality=speciality, appointment_date=dateap, appointment_start_time=start_time, appointment_end_time=end_time)
        appointment.save()



        # saving the appointment in google calender

        SECRET_FILE = "C:\\Users\\nikhi\\OneDrive\\Desktop\\task 3\\user\\client_secret.json"
        API_NAME = "calendar"
        API_VERSION = "v3"
        SCOPES = ['https://www.googleapis.com/auth/calendar']



        service = Create_Service(SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        # try:
        #     event = {
        #         'summary': f'Appointment request for {speciality}',
        #         'location': '800 Howard St., San Francisco, CA 94103',
        #         'start': {
        #             'dateTime': f'{dateap}T09:00:{start_time}:00',
        #             'timeZone': 'GMT',
        #         },
        #         'end': {
        #             'dateTime': f'{dateap}T17:00:{end_time}:00',
        #             'timeZone': 'GMT',
        #         },
        #         'recurrence': [
        #             'RRULE:FREQ=DAILY;COUNT=2'
        #         ],
        #         'attendees': [
        #             {'email': 'lpage@example.com'},
        #             {'email': 'sbrin@example.com'},
        #         ],
        #         'reminders': {
        #             'useDefault': False,
        #             'overrides': [
        #             {'method': 'email', 'minutes': 24 * 60},
        #             {'method': 'popup', 'minutes': 10},
        #             ],
        #         },
        #         }
        #     event = service.events().insert(calendarId='primary', body=event).execute()
        #     print(f"event created: {event}")
        # except Exception as e:
        #     print(e)



        return redirect(f"/confirmap/{appointment.id}")

    return render(request, "bookap.html", {"doc": doc})



def confirmap(request, id):

    appointment = Appointment.objects.get(id=id)

    return render(request, "confirmap.html", {"ap": appointment})