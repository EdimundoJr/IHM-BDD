from behave import given, when, then
from controle import *


@given('o ambiente de reconhecimento seja preparado com sucesso')
def given_ambiente_reconhecimento_preparado(context):
    preparado, context.configuracao = preparar()
    
    assert preparado


@when('a foto {foto} de visitantes for capturada')
def when_foto_de_visitantes_capturada(context, foto):
    context.visitantes = simular_visitas(foto)
    _, context.alunos_reconhecidos = reconhecer_alunos(context.configuracao, context.visitantes)

    assert context.visitantes is not None


@then('pelo menos, um(a) aluno deve ser reconhecido(a)')
def then_um_aluno_reconhecido(context):
    assert context.alunos_reconhecidos is not None and len(context.alunos_reconhecidos) > 0
    
    
@then("pelo menos, um(a) visitante deve ser reconhecido(a)")
def then_um_visitante_reconhecido(context):
    visitantes_reconhecidos, context.alunos_reconhecidos = reconhecer_visitantes(context.alunos_reconhecidos)

    assert visitantes_reconhecidos

@then('nehum aluno reconhecido')
def then_aluno_nao_reconhecido(context):
    alunos_reconhecidos, _ = reconhecer_alunos(
        context.configuracao, context.visitantes)

    assert not alunos_reconhecidos
    
    
 
@then('{total_de_reconhecimentos} alunos deve(m) ser reconhecidos')
def then_total_de_alunos_reconhecidos(context, total_de_reconhecimentos):
    _, context.alunos = reconhecer_alunos(context.configuracao, context.visitantes)

    assert len(context.alunos) == int(total_de_reconhecimentos)
