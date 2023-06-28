Feature: reconhecimento de alunos ao entrar no refeitorio

  Scenario: Um aluno chega na refeitorio da instituicao e deve ser reconhecido por uma camera
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/maevi.jpg de visitantes for capturada
  Then pelo menos, um(a) aluno deve ser reconhecido(a)
  Then pelo menos, um(a) visitante deve ser reconhecido(a)
  When a probabilidade do aluno entrar no refeitorio for 100 porcento
  Then pelo menos, um(a) aluno deve entrar no refeitorio

 Scenario: um aluno está saindo do refeitorio
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/maevi.jpg de visitantes for capturada
  Then pelo menos, um(a) aluno deve ser reconhecido(a)
  Then pelo menos, um(a) visitante deve ser reconhecido(a)
  When a probabilidade do aluno entrar no refeitorio for 0 porcento
  Then nenhum aluno entrou no refeitorio


