from behave import when, then
from controle import *

@when("a probabilidade do aluno entrar no refeitorio for {probabilidade} porcento")
def when_probabilidade_de_sair(context, probabilidade):
   context.total_de_alunos_refeitorio = aluno_no_refeitorio(context.alunos_reconhecidos, int(probabilidade))
   
@then("pelo menos, um(a) aluno deve entrar no refeitorio")
def then_alunos_entrou_refeitorio(context):
    assert context.total_de_alunos_refeitorio > 0
 
@then("nenhum aluno entrou no refeitorio")
def then_aluno_nao_entrou_na_cantina(context):
    assert context.total_de_alunos_refeitorio == 0
