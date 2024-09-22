from django.shortcuts import render, redirect, get_object_or_404 # Importa o render, redirect e o get_object_or_404
from .models import Topic, Entry # Importa o modelo Topic e Entry
from .forms import TopicForm, EntryForm  # Importa o formulário
from django.http import HttpResponseRedirect, Http404 # Importa o HttpResponseRedirect
from django.urls import reverse # Cria um caminho reverso
from django.contrib.auth.decorators import login_required
# Não deixa o usuário acessar a página sem estar logado 
# O decorator é uma forma simples de alterar o comportamento de uma função sem ter a necessidade de modificar o código


def index(request):
    """A página inicial do Learning Log"""
    return render(request, 'learning_logs/index.html') 

@login_required
def topics(request):
    """Mostra todos os assuntos"""
    # Pega a informação do banco de dados de Topics e filtra pelo o User logado e ordena pelo campo date_added 
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
@login_required
def topic(request, topic_id):
    """Mostra um tópico específico"""
    topic = Topic.objects.get(id=topic_id)
   
    # Garante que o tópico pertence ao usuário
    if topic.owner != request.user:
        raise Http404
    else:
        entries = topic.entry_set.order_by('-date_added')
        # Cria um dicionário a partir dos valores da tabela Topic
        context = {'topic': topic, 'entries': entries} 
        print(context)
        return render(request, 'learning_logs/topic.html', context)

# Create do CRUD
@login_required
def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado foi enviado; crie um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST foram enviados; processa os dados
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # Salva o formulário, mas não salva no banco de dados ainda
            new_topic = form.save(commit=False)
            # Define o dono do tópico como o usuário que fez a requisição
            new_topic.owner = request.user
            # Agora é salvo o tópico
            new_topic.save()
            # Redireciona para a página topics
            return HttpResponseRedirect(reverse(topics))

    # Mostra o formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

# Create do CRUD
@login_required
def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um tópico específico"""
    topic = Topic.objects.get(id=topic_id) # Pega o tópico que o usuário escolheu

    # Garante que o tópico pertence ao usuário
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Nenhum dado foi enviado; crie um formulário em branco
        form = EntryForm()
    else:
        # Dados de POST foram enviados; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Salva o formulário, mas não salva no banco de dados ainda "commit=False"
            new_entry = form.save(commit=False) 
            # Adiciona o tópico ao formulário
            new_entry.topic = topic 
            # Salva no banco de dados
            new_entry.save() 
            # Redireciona para a página topics
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    # Mostra o formulário em branco ou inválido
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# Update do CRUD
@login_required
def edit_entry(request, entry_id):
    """
    Edita uma entrada existente. Isso é o Update do CRUD.
    """
    # Pega a entrada que o usuário deseja editar
    entry = Entry.objects.get(id=entry_id)
    # Pega o tópico ao qual a entrada pertence
    topic = entry.topic
    
    # Garante que o tópico pertence ao usuário
    if topic.owner != request.user:
        raise Http404   
    
    # Verifica se o método da requisição é POST
    if request.method != 'POST':
        # Se não for POST, preenche o formulário com os dados atuais da entrada
        form = EntryForm(instance=entry)
    else:
        # Se for POST, processa os dados e salva a entrada
        # instance=entry é para preencher o formulário com os dados atuais
        form = EntryForm(instance=entry, data=request.POST)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Se for válido, salva a entrada
            form.save()
            # Redireciona para a página do tópico ao qual a entrada pertence
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    # Mostra o formulário em branco ou inválido
    # Passa o tópico, a entrada e o formulário para o template
    context = {'topic': topic, 'entry': entry, 'form': form}
    # Renderiza o template edit_entry.html com o contexto
    return render(request, 'learning_logs/edit_entry.html', context)

# Delete do CRUD
@login_required
def delete_topic(request, topic_id):
    """Apaga um tópico específico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method == 'GET':
        context = {'topic': topic}
        return render(request, 'learning_logs/delete_topic.html', context)  
    elif request.method == 'POST':  
        topic.delete()
        return redirect('index')

    # Se o método for POST, deleta o tópico
    topic.delete()
    return HttpResponseRedirect(reverse('index'))
