Feature: reconhecimento de alunos ao sair no refeitorio

  Scenario: Um aluno sai do refeitorio da instituicao e deve ser reconhecido por uma camera
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/maevi.jpg de visitantes for capturada
  Then pelo menos, um(a) aluno deve ser reconhecido(a)
  Then pelo menos, um(a) visitante deve ser reconhecido(a)
  When a probabilidade do aluno sair do refeitorio for 100 porcento
  Then pelo menos, um(a) aluno deve sair do refeitorio

 Scenario: um aluno está saindo do refeitorio
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/maevi.jpg de visitantes for capturada
  Then pelo menos, um(a) aluno deve ser reconhecido(a)
  Then pelo menos, um(a) visitante deve ser reconhecido(a)
  When a probabilidade do aluno sair do refeitorio for 0 porcento
  Then nenhum aluno saiu do refeitorio


