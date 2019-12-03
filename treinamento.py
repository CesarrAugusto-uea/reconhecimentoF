import cv2
import os
import numpy as np


def treinarAlgo():

    eigenface = cv2.face.EigenFaceRecognizer_create(num_components=75 , threshold=0)
    fisherface = cv2.face.FisherFaceRecognizer_create(num_components=75 , threshold=0)
    lbph = cv2.face.LBPHFaceRecognizer_create(threshold=0)


    def getImagemComId():       #percorre todas as imagens na pasta de fotos
        caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]

        faces = []   #faces de cada pessoa
        ids = []    #id de cada pessoa
        for caminhoImagem in caminhos:
            imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)

            id = int(os.path.split(caminhoImagem)[-1].split('.')[1])

            ids.append(id)
            faces.append(imagemFace)


        return np.array(ids), faces      #retorna as imagens e seus respectivos ids
    ids, faces = getImagemComId()
#print(ids)
#print(faces)


    print("Treinando....")

    eigenface.train(faces, ids)        #método responsável pelo treinamento do algoritmo, recebe as listas de faces e o ids
    eigenface.write('classificadorEigen.yml')

    fisherface.train(faces, ids)
    fisherface.write ('classificadorFisher.yml')

    lbph.train(faces, ids)
    lbph.write ('classificadorLbph.yml')

    print('Treinamento realizado...')



