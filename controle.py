import face_recognition as reconhecedor
import colored
import secrets
import random
import json

ARQUIVO_DE_CONFIGURACAO = "configuracao.json"


def preparar():

    preparado, configuracao = False, None
    try:
        with open(ARQUIVO_DE_CONFIGURACAO, "r", encoding='utf-8') as arquivo:
            configuracao = json.load(arquivo)
            if configuracao:
                print("*---Carregado os aquivos de configuração!---*")
            arquivo.close()

            preparado = True
    except Exception as e:
        print(f"--> erro ao fazer a leitura do: {str(e)}")

    return preparado, configuracao


def simular_visitas(foto):
    print(f"--foto de visitantes: {foto}")

    visitantes = {
        "foto": foto,
        "alunos": None,
        "intrusos": None
    }

    return visitantes


def reconhecer_alunos(configuracao, visitantes):
    foto_visitantes = reconhecedor.load_image_file(visitantes["foto"])
    caracteristicas_dos_visitantes = reconhecedor.face_encodings(
        foto_visitantes)

    alunos = []
    for aluno in configuracao["alunos"]:
        fotos = aluno["fotos"]
        num_faces_reconhecidas = 0

        for foto in fotos:
            foto_aluno = reconhecedor.load_image_file(foto)
            caracteristicas_aluno = reconhecedor.face_encodings(foto_aluno)[0]

            reconhecimentos = reconhecedor.compare_faces(
                caracteristicas_dos_visitantes, caracteristicas_aluno)
            if True in reconhecimentos:
                num_faces_reconhecidas += 1

        if num_faces_reconhecidas / len(fotos) >= 0.6:
            alunos.append(aluno)

    return len(alunos) > 0, alunos



def reconhecer_intrusos(configuracao, visitantes):
    

    print("Realizando reconhecimento dos intrusos...")
    foto_visitantes = reconhecedor.load_image_file(visitantes["foto"])
    caracteristicas_dos_visitantes = reconhecedor.face_encodings(
        foto_visitantes)

    intrusos = []

    for intruso in configuracao["intrusos"]:

        fotos = intruso["fotos"]
        num_faces_reconhecidas = 0

        for foto in fotos:
            foto_intruso = reconhecedor.load_image_file(foto)
            caracteristicas_intruso = reconhecedor.face_encodings(foto_intruso)

            
            reconhecimentos = reconhecedor.compare_faces(
                caracteristicas_dos_visitantes, caracteristicas_intruso[0])
            if True in reconhecimentos:
                num_faces_reconhecidas += 1

        if num_faces_reconhecidas / len(fotos) >= 0.6:
            intrusos.append(intruso)

    return len(intrusos) > 0, intrusos



def imprimir_dados_do_aluno(aluno):
    print(colored.fg('black'), colored.bg(
        'blue'), f"aluno reconhecido", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'blue'), f"nome: {aluno['nome']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'blue'), f"curso: {aluno['curso']}", colored.attr('reset'))


def imprimir_dados_do_intruso(intruso):
    print(colored.fg('black'), colored.bg(
        'red'), f"intruso reconhecido", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'red'), f"nome: {intruso['nome']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'red'), f"curso: {intruso['curso']}", colored.attr('reset'))


def reconhecer_visitantes(alunos_reconhecidos):
    visitantes_reconhecidos = {}

    for aluno in alunos_reconhecidos:
        aluno["na_instituicao"] = False
        aluno["no_refeitorio"] = False
        
        id_entrada = secrets.token_hex(nbytes=16).upper()
        visitantes_reconhecidos[id_entrada] = aluno

        imprimir_dados_do_aluno(aluno)

    

    return len(visitantes_reconhecidos) > 0, visitantes_reconhecidos


def saida_alunos(alunos_reconhecidos, probabilidade_de_liberacao):
    total_alunos_saindo = 0

    for id_entrada, aluno in list(alunos_reconhecidos.items()):
        if not aluno["na_instituicao"]:
            aluno_liberado = (random.randint(
                1, 100) <= probabilidade_de_liberacao)
            if aluno_liberado:
                alunos_reconhecidos.pop(id_entrada)

                total_alunos_saindo += 1

    return total_alunos_saindo



def aluno_no_refeitorio(alunos_reconhecidos, probabilidade_ir_ao_refeitorio):
    total_de_alunos_refeitorio = 0
    
    
    for aluno in alunos_reconhecidos.values():
        if aluno["na_instituicao"] and not aluno["no_refeitorio"]:
            enviar_pro_refeitorio = (random.randint(
                        1, 100)) <= probabilidade_ir_ao_refeitorio
            if enviar_pro_refeitorio:
                aluno["no_refeitorio"] = True
                        
                total_de_alunos_refeitorio += 1
                        
    return total_de_alunos_refeitorio
   
   
def aluno_saida_refeitorio(alunos_reconhecidos,probabilidade_de_liberacao_do_refeitorio):
    
    saida_alunos_refeitorio = 0
    for aluno in alunos_reconhecidos.values():
        if aluno["no_refeitorio"]:
            aluno_liberado = (random.randint(
                        1, 100)) <= probabilidade_de_liberacao_do_refeitorio
            if aluno_liberado:
                aluno["no_refeitorio"] = False
                saida_alunos_refeitorio += 1
        
    return saida_alunos_refeitorio


def alunos_refeitorio(alunos_reconhecidos):
   
    alunos_no_refeitorio = 0
    for aluno in alunos_reconhecidos.values():
        if aluno["no_refeitorio"]:
            alunos_no_refeitorio += 1

    return alunos_no_refeitorio
