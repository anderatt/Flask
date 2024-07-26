class CPF():

    def __init__(self, numCPF):
        self.numCPF = numCPF

    def tamanhoDado(numDado):
        tamanho=len(numDado)
        bOK=True
        if (tamanho != 11) and (tamanho != 14):
            print("Tamanho dos dados errado!!")
            bOK=False
        return bOK
    
    def validaCPF(numCPF):
        if CPF.tamanhoDado(numCPF):
            soma1P=0
            #for x in range(len(numCPF)):
            for x in range(9):
                soma1P = soma1P + (int(numCPF[x]) * (10-x))
            resto1P = soma1P % 11
            digVerificador1 = 11 - resto1P 
            if digVerificador1 >= 10:
                digVerificador1=0

            soma2P=0
            #for x in range(len(numCPF)):
            for x in range(10):
                soma2P = soma2P + (int(numCPF[x]) * (11-x))
            resto2P = soma2P % 11
            digVerificador2 = 11 - resto2P 
            if digVerificador2 >= 10:
                digVerificador2=0
            digFinal=(digVerificador1 * 10) + digVerificador2
            
            bOK=True

            if digFinal != int(numCPF[9:11]):
                print("CPF Inválido")
                bOK=False
            
        return bOK

            
            


        

CPF.validaCPF("09782594830")