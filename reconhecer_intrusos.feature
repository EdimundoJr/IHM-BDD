Feature: reconhecimento de intrusos

  Scenario: Um visitante chega na portaria da instituicao e deve ser reconhecido por uma camera
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/Olivia.jpg de visitantes for capturada
  Then nehum intruso reconhecido

  Scenario: Uma pessoa chega na portaria da instituicao e nao deve ser reconhecido por uma camera
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto faces/Aimee2.jpg de intrusos for capturada
  Then pelo menos, um(a) intruso deve ser reconhecido(a)

  Scenario Outline: reconhecer intrusos de varias fotos diferentes
  Given o ambiente de reconhecimento seja preparado com sucesso
  When a foto <foto_capturada> de visitantes for capturada
  Then <total_de_reconhecimentos> intrusos deve(m) ser reconhecidos

  Examples:
  | foto_capturada          | total_de_reconhecimentos |
  | faces/visitantes1.jpg   | 0                        |
  | faces/visitantes2.jpg   | 1                        |
  | faces/visitantes3.jpg   | 2                        |

