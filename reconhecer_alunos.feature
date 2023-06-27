Feature: reconhecimento de alunos

  Scenario: Um aluno chega na portaria da instituicao e deve ser reconhecido por uma camera
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/maevi.jpg de visitantes for capturada
  Then pelo menos, um(a) aluno deve ser reconhecido(a)

  Scenario: Uma pessoa chega na portaria da instituicao e nao deve ser reconhecido por uma camera
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/Olivia.jpg de visitantes for capturada
  Then nehum aluno reconhecido

  Scenario Outline: reconhecer alunos de varias fotos diferentes
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto <foto_capturada> de visitantes for capturada
  Then <total_de_reconhecimentos> alunos deve(m) ser reconhecidos

  Examples:
  | foto_capturada          | total_de_reconhecimentos |
  | faces/visitantes1.jpg   | 0                        |
  | faces/visitantes2.jpg   | 2                        |
  | faces/visitantes3.jpg   | 3                        |

