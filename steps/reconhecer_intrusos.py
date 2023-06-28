from behave import   when,then
from controle import *

 
@when('a foto {foto} de intrusos for capturada')
def when_foto_de_visitantes_capturada(context, foto):
    context.visitantes = simular_visitas(foto)
    _, context.intrusos_reconhecidos = reconhecer_intrusos(context.configuracao, context.visitantes)

    assert context.visitantes is not None
    
@then('pelo menos, um(a) intruso deve ser reconhecido(a)')
def then_um_intruso_reconhecido(context):
  assert context.intrusos_reconhecidos  is not None and len(context.intrusos_reconhecidos ) > 0 

@then('nehum intruso reconhecido')
def then_intruso_nao_reconhecido(context):
    intrusos_reconhecidos, _ = reconhecer_intrusos(
        context.configuracao, context.visitantes)

    assert not intrusos_reconhecidos      
 
@then('{total_de_reconhecimentos} intrusos deve(m) ser reconhecidos')
def then_total_de_intrusos_reconhecidos(context, total_de_reconhecimentos):
    _, context.intrusos = reconhecer_intrusos(context.configuracao, context.visitantes)

    assert len(context.intrusos) == int(total_de_reconhecimentos)