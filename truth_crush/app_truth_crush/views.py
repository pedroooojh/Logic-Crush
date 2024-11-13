import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'app_truth_crush/index.html')

def nivel1(request):
    return render(request, 'app_truth_crush/nivel1.html')

def nivel2(request):
    return render(request, 'app_truth_crush/nivel2.html')

def nivel3(request):
    return render(request, 'app_truth_crush/nivel3.html')



def atualizar_pontuacao(request):
    if request.method == 'POST':
        # Receber dados enviados pelo AJAX
        pontos = int(request.POST.get('pontos', 0))
        nivel_atual = int(request.session.get('nivel', 1))  # Recuperar nível da sessão
        proximo_nivel = False

        # Lógica para progressão de nível
        if pontos >= 10:
            nivel_atual += 1
            pontos = 0  # Reiniciar pontos ao avançar de nível
            proximo_nivel = True

        # Atualizar dados na sessão
        request.session['nivel'] = nivel_atual
        request.session['pontos'] = pontos

        return JsonResponse({
            'nivel': nivel_atual,
            'nivel_atualizado': proximo_nivel,
        })

    return JsonResponse({'error': 'Método não permitido'}, status=400)
