from behave import when, then
from controle import *

@when("a probabilidade do aluno sair do refeitorio for {probabilidade} porcento")
def when_probabilidade_de_sair(context, probabilidade):
   context.saida_alunos_refeitorio = aluno_saida_refeitorio(context.alunos_reconhecidos, int(probabilidade))
   
@then("pelo menos, um(a) aluno deve sair do refeitorio")
def then_aluno_saida_refeitorio(context):
    assert context.saida_alunos_refeitorio > 0
 
@then("nenhum aluno saiu do refeitorio")
def then_nhnum_aluno_saiu_do_refeitorio(context):
    assert context.saida_alunos_refeitorio == 0
