import json
from uuid import UUID

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

from django.core.serializers import serialize

from codes.models import CodesUser, Meeting


def event_cities(request):
    return JsonResponse(
        {'data':
            [
                {'cityName': 'Москва'},
                {'cityName': 'Санкт-Петербург'}
            ]
        })


@csrf_exempt
def reg_user(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        user = User.objects.create_user(
            username=data['email'],
            email=data['email'],
            password=data['password'],
            first_name=data['fname'],
            last_name=data['lname'],
        )
    return HttpResponse(status=200)


@csrf_exempt
def login_user(request: HttpRequest):
    data = json.loads(request.body)
    print(data)
    user = authenticate(username=data['email'], password=data['password'])
    if user is not None:
        login(request, user)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


@csrf_exempt
@login_required
def create_profile(request):
    data = json.loads(request.body)
    profile = CodesUser(
        user=request.user,
        phone_number=data['phone'],
        education=data['education'],
        organization=data['organization'],
        specification=data['specification'],
        position=data['position'],
        experience=data['experience'],
        interests=data['interests'],
    )
    profile.save()
    return JsonResponse({'id': request.user.pk})


@csrf_exempt
@login_required
def upload_profile_pic(request):
    pic = request.FILES['pic']
    profile = CodesUser.objects.get(user=request.user)
    pic.name = 'userpic_' + str(request.user.pk) + '.jpg'
    profile.profile_pic = pic
    profile.save()
    return JsonResponse({'success': True})


@csrf_exempt
def get_user(request):
    user_id = int(request.GET['uid'])
    if int(user_id) == 0 and request.user:
        print(request.user)
        user_id = request.user.pk

    print(user_id)
    try:
        user = User.objects.get(pk=user_id)
    except:
        user = None
    if user:
        profile = CodesUser.objects.get(user=user)
        return JsonResponse(
            {
                'pic': profile.profile_pic.url,
                'phone': profile.phone_number,
                'education': profile.education,
                'experience': profile.experience,
                'organization': profile.organization,
                'position': profile.position,
                'specification': profile.specification,
                'interests': profile.interests,
                'telegram': profile.telegram,
                'fname': user.first_name,
                'lname': user.last_name,
                'email': user.email,
            }
        )
    return JsonResponse({})


@csrf_exempt
def get_all_users(request):
    profiles = CodesUser.objects.all()

    res = [{
        'uid': obj.user.pk,
        'fname': obj.user.first_name,
        'lname': obj.user.last_name,
        'pic': obj.profile_pic.url,
        'organization': obj.organization
    } for obj in profiles]

    return JsonResponse(res, safe=False)


@csrf_exempt
def get_all_events(request):
    events = Meeting.objects.all()
    res = [{
        'id': obj.pk,
        'title': obj.title,
        'preview_desc': obj.preview_desc,
        'timestamp': obj.timestamp,
        'city': obj.city,
        'preview_img': obj.preview_img.url
    } for obj in events]
    return JsonResponse(res, safe=False)


@csrf_exempt
def get_event(request):
    if 'id' in request.GET:
        event = Meeting.objects.get(pk=request.GET['id'])
    else:
        return JsonResponse({})
    res = {
        'title': event.title,
        'preview_desc': event.preview_desc,
        'timestamp': event.timestamp,
        'city': event.city,
        'preview_img': event.preview_img.url,
        'lat': event.lat,
        'lng': event.lng,
        'main_img': event.main_img.url,
        'full_desc': event.full_desc
    }

    return JsonResponse(res)


@csrf_exempt
def create_event(request):
    data = json.loads(request.body)
    print(data)
    meeting = Meeting(
        title=data['title'],
        preview_desc=data['desc'],
        timestamp=data['timestamp'],
        city=data['city'],
        lat=data['geotag']['lat'],
        lng=data['geotag']['lng'],
        full_desc=data['fullDescription']
    )

    meeting.save()

    return JsonResponse({'id': meeting.pk})
    # {'title': 'ЧИЛЛЛЛ',
    # 'desc': 'Summary',
    #  'timestamp': '2020-01-16T10:15:16.807Z',
    #  'city': 'Moscow',
    #  'geotag':
    #  {'lng': 37.537351, 'lat': 55.837347},
    #  'fullDescription': 'фывфыв'}


@csrf_exempt
def event_main(request, pk):
    pic = request.FILES['pic']
    event = Meeting.objects.get(pk=pk)
    pic.name = 'event_main_' + str(pk) + '.jpg'
    event.main_img = pic
    event.save()
    return JsonResponse({'success': True})


@csrf_exempt
def event_preview(request, pk):
    pic = request.FILES['pic']
    event = Meeting.objects.get(pk=pk)
    pic.name = 'event_preview_' + str(pk) + '.jpg'
    event.preview_img = pic
    event.save()
    return JsonResponse({'success': True})


@csrf_exempt
def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({'authorized': True})
    else:
        return JsonResponse({'authorized': False})


@csrf_exempt
def user_logout(request):
    logout(request)


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
