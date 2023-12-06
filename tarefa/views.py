from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect


def List(request):
    if request.method == 'POST':
        tarefa_id = request.POST.get('tarefa_id')
        if tarefa_id:
            tarefa = get_object_or_404(Tarefas, id=tarefa_id)

            tarefa.status = not tarefa.status
            tarefa.save()

            return HttpResponseRedirect(request.path)

    tarefas = {
        'tarefas': Tarefas.objects.all(),
    }
    return render(request, 'tarefas/listTarefas.html', tarefas)



def Create(request):
    nome = ''
    email = ''
    descricao = ''

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        descricao = request.POST.get('descricao')

        existe_tarefa = Tarefas.objects.filter(nome=nome, email=email, descricao=descricao).first()

        if not existe_tarefa:
            tarefa = Tarefas(nome=nome, email=email, descricao=descricao)
            tarefa.save()

            data = {
                'nome': request.POST.get('nome'),
                'email': request.POST.get('email'),
                'descricao': request.POST.get('descricao'),
            }
            Email(data)

            return redirect('List')

    tarefas = {
        'tarefas': Tarefas.objects.all(),
    }

    return render(request, 'tarefas/home.html', tarefas)



def Email(data):
    message_body = get_template('tarefas/email.html').render(data)
    sendmail = EmailMessage('Cadastro Feito com Sucesso', message_body, settings.DEFAULT_FROM_EMAIL, to=['lturco@hotmail.com'])
    sendmail.content_subtype = 'html'
    return sendmail.send()  



def Edit(request, id):
    tarefa = Tarefas.objects.get(id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        descricao = request.POST.get('descricao')

        existe_tarefa = Tarefas.objects.exclude(id=id).filter(nome=nome, email=email, descricao=descricao).first()

        if not existe_tarefa:
            tarefa.nome = nome
            tarefa.email = email
            tarefa.descricao = descricao
            tarefa.save()

            return redirect('List')

    tarefas = {'tarefas': Tarefas.objects.all()}

    return render(request, 'tarefas/editTarefas.html', {'tarefa': tarefa, **tarefas})
    


def Delete(request, id):
    tarefa = Tarefas.objects.get(id=id)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('List')
    
    return render(request, 'tarefas/confirmDelete.html', {'tarefa': tarefa})
