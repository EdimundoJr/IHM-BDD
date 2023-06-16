Feature: verificando se existem alunos para sair da Instiruicao

    Scenario: um aluno está indo embora
    Given o ambiente de reconhecimento seja preparado com sucesso
    When a foto faces/visitantes3.jpg de visitantes for capturada
    Then pelo menos, um(a) aluno deve ser reconhecido(a)
    Then pelo menos, um(a) visitante deve ser reconhecido(a)
    When a probabilidade de sair for 100 porcento
    Then pelo menos, um(a) aluno deve sair

    Scenario: um aluno está indo embora
    Given o ambiente de reconhecimento seja preparado com sucesso
    When a foto faces/visitantes3.jpg de visitantes for capturada
    Then pelo menos, um(a) aluno deve ser reconhecido(a)
    Then pelo menos, um(a) visitante deve ser reconhecido(a)
    When a probabilidade de sair for 0 porcento
    Then nenhum aluno deve sair

