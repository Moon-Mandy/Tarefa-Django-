from django.shortcuts import render, redirect
from Site_app.models import Pessoa

def home(request):
    # Método executado quando o usuário está na interface inicial do sistema home.html
    return render(request, "home.html")

def registrarPessoa(request):
    if request.method == 'POST':
        # Criação da aluna como instância da classe Aluna definida no modelo de classes
        nome = request.POST.get('nomePessoa')
        sobrenome = request.POST.get('sobrenomePessoa')
        telefone = request.POST.get('telefonePessoa')
        estado = request.POST.get('estadoPessoa')
        

        # Cria e salva a nova instância de Aluna
        nova_pessoa = Pessoa(nomePessoa=nome, sobrenomePessoa=sobrenome, telefonePessoa=telefone, estadoPessoa=estado)
        nova_pessoa.save()

        # Redireciona para a página inicial ou outra página de confirmação
        return redirect('home')  # Substitua 'home' pela URL da sua página inicial ou outra página

    # Renderiza o formulário caso seja uma requisição GET
    return render(request, 'home.html')
