from django.shortcuts import render
from .bertify import generate_answer, generate_summary
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            answer = generate_answer(question)
            summary = generate_summary(answer) 
            title = ' '.join(question.split()[:5])
            chat = Chat(question=question, answer=answer, title=title, summary=summary)
            chat.save()
        answer = generate_answer(question)
        return render(request, 'home/index.html', {'question': question, 'answer': answer})
    return render(request, 'home/index.html')

def chat_history_view(request):
    chats = Chat.objects.all().order_by('-timestamp')
    chat_titles = chats.values('id', 'title')
    return render(request, 'home/chat_history.html', {'chats': chats, 'chat_titles': chat_titles})

def chat_detail_view(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    return render(request, 'home/chat_detail.html', {'chat': chat})