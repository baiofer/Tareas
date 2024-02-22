from django.shortcuts import render, redirect  # type: ignore
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """La página de inicio para learning_log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Muestra todos los temas"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Muestra un tema concreto y todas sus entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    print(request)
    """Añade un nuevo tema"""
    if request.method != 'POST':
        """No se han enviado datos. Crea un formulario en blanco"""
        form = TopicForm()
    else: 
        """Datos POST enviados. Procesa datos"""
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    # Muestra un formulario no válido
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Añade una entrada nueva para un tema en particular"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        """No se han enviado datos. Crea un formulario en blanco"""
        form = EntryForm()
    else: 
        """Datos POST enviados. Procesa los datos"""
        form = EntryForm(data=request.POST)
        if form.is_valid():
            print('ES BUENOOOOO !!!!!')
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    """Muestra un formulario en blanco o no válido"""
    print(topic)
    context = {'topic': topic, 'form': form}
    return (render(request, 'learning_logs/new_entry.html', context))


def edit_entry(request, entry_id):
    """Edita una entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # Solicitud inicial, prerrellena el formulario con la entrada actual
        form = EntryForm(instance=entry)
    else:
        # Datos POST enviados, procesar datos
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
