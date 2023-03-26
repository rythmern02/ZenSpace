from django.shortcuts import render
from googleapiclient.discovery import build
from trendc.secrets import GOOGLE_API_KEY
from django.http import JsonResponse


def search(request):
    query = request.GET.get('q')
    if query:
        youtube = build('youtube', 'v3', developerKey=GOOGLE_API_KEY)
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=10
        ).execute()
        videos = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append(search_result)
        return render(request, 'search_results.html', {'videos': videos, 'query': query})
    else:
        return render(request, 'search.html')


def trending_programming_courses(request):
    api_key = GOOGLE_API_KEY
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        q='programming courses',
        type='video',
        videoDefinition='high',
        videoCategoryId='27',  # Category ID for Education
        regionCode='US',
        maxResults=10  # Number of results to return
    )
    response = request.execute()

    items = response['items']
    course_list = []
    for item in items:
        course = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'thumbnail_url': item['snippet']['thumbnails']['default']['url'],
            'video_url': f'https://www.youtube.com/watch?v={item["id"]["videoId"]}',
        }
        course_list.append(course)

    return JsonResponse(course_list, safe=False)



def trending_music_courses(request):
    api_key = GOOGLE_API_KEY
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        q='music courses',
        type='video',
        videoDefinition='high',
        videoCategoryId='27',  # Category ID for Education
        regionCode='US',
        maxResults=10  # Number of results to return
    )
    response = request.execute()

    items = response['items']
    course_list = []
    for item in items:
        course = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'thumbnail_url': item['snippet']['thumbnails']['default']['url'],
            'video_url': f'https://www.youtube.com/watch?v={item["id"]["videoId"]}',
        }
        course_list.append(course)

    return JsonResponse(course_list, safe=False)

def trending_education_courses(request):
    api_key = GOOGLE_API_KEY
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        q='education courses',
        type='video',
        videoDefinition='high',
        videoCategoryId='27',  # Category ID for Education
        regionCode='US',
        maxResults=10  # Number of results to return
    )
    response = request.execute()

    items = response['items']
    course_list = []
    for item in items:
        course = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'thumbnail_url': item['snippet']['thumbnails']['default']['url'],
            'video_url': f'https://www.youtube.com/watch?v={item["id"]["videoId"]}',
        }
        course_list.append(course)

    return JsonResponse(course_list, safe=False)


