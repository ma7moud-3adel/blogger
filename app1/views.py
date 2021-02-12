from django.shortcuts import render

posts = [
	{
		'author': 'Ahmed',
		'title':'Morning',
		'content': 'Good Morning everyone, How are you doing',
		'date': '11-2-2021'
	},
	{
		'author': 'Ali',
		'title':'Marriage',
		'content': 'I have finally accomplished the miracle of Marriage',
		'date': '12-2-2021'
	},
	{
		'author': 'Mahmoud',
		'title':'New Baby',
		'content': 'I am a Father now :D',
		'date': '13-2-2021'
	}
]


def home(request):
	context={
		'posts': posts,
		'title': 'Home'
	}
	return render(request, 'blog/home.html', context)

def profile(request):
	return render(request, 'blog/profile.html', {'title': 'Profile'})

def friends(request):
	return render(request, 'blog/friends.html', {'title': 'Friends'})
