from django.shortcuts import render

def home(request):
    cards = [
        {
            'img': 'images/skillsteps.png',
            'alt': 'learn explore grow',
            'icon': 'bi-leaf',
            'title': 'Grow Through Teaching',
            'desc': 'Share your expertise and boost your skills by helping others.',
            'aos_animation': 'fade-left',
            'aos_delay': '250',
        },
        {
            'img': 'images/skill_swap.jpg',
            'alt': 'swap skills',
            'icon': 'bi-arrow-repeat',
            'title': 'Swap Skills Effortlessly',
            'desc': 'Find partners based on interest, location, and availability.',
            'aos_animation': 'zoom-in',
            'aos_delay': '300',
        },
        {
            'img': 'images/skill.jpg',
            'alt': 'learning is important',
            'icon': 'bi-airplane',
            'title': 'Learn What Matters',
            'desc': 'Get practical knowledge from real practitioners.',
            'aos_animation': 'fade-right',
            'aos_delay': '250',
        },
    ]
    return render(request, 'home.html', {'cards': cards})


def about(request):
    return render(request, 'about.html')