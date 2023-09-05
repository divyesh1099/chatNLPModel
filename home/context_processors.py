from .models import *

def chat_history_context_processor(request):
    chats = Chat.objects.all().order_by('-timestamp')
    chat_titles = chats.values('id', 'title')
    context = {'chats': chats, 'chat_titles': chat_titles}
    return context