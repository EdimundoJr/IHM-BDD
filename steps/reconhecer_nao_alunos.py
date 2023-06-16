from behave import  then
from controle import *



@then('nenhum visitante desconhecido')
def then_nenhum_visitante_aceito(context,num_faces_desconhecidas):
    barrados, context.alunos_reconhecidos = barrar_intruso(context.alunos_reconhecidos,num_faces_desconhecidas)
    
    barrados == 0
