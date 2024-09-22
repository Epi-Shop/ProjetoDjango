from django import forms
from .models import Topic, Entry # Importa o modelo Topic e Entry

class TopicForm(forms.ModelForm):
    class Meta: # Classe que vai permitir a criação de um formulário, utilizando os dados da tabela Topic
        # Cria o modelo do formulário com os dados da tabela Topic
        model = Topic 
        # Cria um formulário com apenas o campo text
        fields = ['text'] 
        labels = {'text': ''} 
        
class EntryForm(forms.ModelForm):
    class Meta:
        # Cria o modelo do formulário com os dados da tabela Entry
        model = Entry 
        fields = ['text']
        labels = {'text': ''}
        #Bloco onde são computados os atributos enviados pelo o usuário
        # attrs = corresponde aos atributos
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} 