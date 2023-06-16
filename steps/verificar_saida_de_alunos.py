from behave import when, then
from controle import *

@when("a probabilidade de sair for {probabilidade} porcento")
def when_probabilidade_de_sair(context, probabilidade):
   context.total_alunos_saindo = saida_alunos(context.alunos_reconhecidos, int(probabilidade))
   
@then("pelo menos, um(a) aluno deve sair")
def then_pacientes_liberados(context):
    assert context.total_alunos_saindo > 0
 
@then("nenhum aluno deve sair")
def then_pacientes_liberados(context):
    assert context.total_alunos_saindo == 0

