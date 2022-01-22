import random

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())


def call():
    # stock at each node
    # Sp - S+
    # Sn - S-
    # Spp - S++
    # Snn = S--
    # S+- = S+-
    Sp = S * (1 + u)
    Sn = S * (1 - d)
    Spp = Sp * (1 + u)
    Spn = Sp * (1 - d)
    Snn = Sn * (1 - d)

    # intrinsic value of the call option at expiration
    # Cp - C+
    # Cn - C-
    # Cpp - C++
    # Cnn = C--
    # C+- = C+-
    Cpp = max(0, Spp - S)
    Cpn = max(0, Spn - S)
    Cnn = max(0, Snn - S)

    # risk neutral probabilities
    π = "003C0"
    π = (1 + r - (1 - d)) / ((1 + u) - (1 - d))

    Cp = ((Cpp * π) + (Cpn * (1 - π))) / (1 + r)
    Cn = ((Cpn * π) + (Cnn * (1 - π))) / (1 + r)

    C = ((Cp * π) + (Cn * (1 - π))) / (1 + r)

    # hedge ratio

    hc = (Cp - Cn) / (Sp - Sn)
    hcp = (Cpp - Cpn) / (Spp - Spn)
    hcn = (Cpn - Cnn) / (Spn - Snn)

    A = ["T=0 ","------", round(S,4), round(C,4), round(hc,4)]
    B = ["T=1 ","---", round(Sp,4), round(Cp,4), round(hcp,4)]
    C = ["T=1 ","---", round(Sn,4), round(Cn,4), round(hcn,4)]
    D = ["T=2 ",round(Spp,4), round(Cpp,4)]
    E = ["T=2 ",round(Spn,4), round(Cpn,4)]
    F = ["T=2 ",round(Snn,4), round(Cnn,4)]

    # Tree_binomial(A,B,C,D,E,F)

    def Tree_BI():
        myTree = BinaryTree("BI")
        myTree.insertRight(F)
        myTree.insertRight(E)
        myTree.insertRight(D)
        myTree.insertRight(C)
        myTree.insertRight(B)
        myTree.insertRight(A)
        printTree(myTree)

    Tree_BI()

def put():
    # stock at each node
    # Sp - S+
    # Sn - S-
    # Spp - S++
    # Snn = S--
    # S+- = S+-
    Sp = S * (1 + u)
    Sn = S * (1 - d)
    Spp = Sp * (1 + u)
    Spn = Sp * (1 - d)
    Snn = Sn * (1 - d)

    # intrinsic value of the call option at expiration
    # Pp - P+
    # Pn - P-
    # Ppp - P++
    # Pnn = P--
    # P+- = P+-
    Ppp = max(0, S - Spp)
    Ppn = max(0, S - Spn)
    Pnn = max(0, S - Snn)

    # risk neutral probabilities
    π = "003C0"
    π = (1 + r - (1 - d)) / ((1 + u) - (1 - d))

    Pp = ((Ppp * π) + (Ppn * (1 - π))) / (1 + r)
    Pn = ((Ppn * π) + (Pnn * (1 - π))) / (1 + r)

    P = ((Pp * π) + (Pn * (1 - π))) / (1 + r)

    # hedge ratio

    hp = (Pp - Pn) / (Sp - Sn)
    hpp = (Ppp - Ppn) / (Spp - Spn)
    hpn = (Ppn - Pnn) / (Spn - Snn)

    A = ["T=0 ","------", round(S,4), round(P,4), round(hp,4)]
    B = ["T=1 ","---", round(Sp,4), round(Pp,4), round(hpp,4)]
    C = ["T=1 ","---", round(Sn,4), round(Pn,4), round(hpn,4)]
    D = ["T=2 ",round(Spp,4), round(Ppp,4)]
    E = ["T=2 ",round(Spn,4), round(Ppn,4)]
    F = ["T=2 ",round(Snn,4), round(Pnn,4)]

    # Tree_binomial(A,B,C,D,E,F)

    def Tree_BI():
        myTree = BinaryTree("BI")
        myTree.insertRight(F)
        myTree.insertRight(E)
        myTree.insertRight(D)
        myTree.insertRight(C)
        myTree.insertRight(B)
        myTree.insertRight(A)
        printTree(myTree)

    Tree_BI()
#print("input exactly the choice (i.e. random call has to be RC")
Choice = input("Random Call (RC), Random Put (RP), Manual Call (MC), Manual Put (MP):")

if Choice == "RC" or Choice == "rc" or Choice == "random call":

    dt = 2  
    S = round(random.uniform(5,150),0)
    r = round(random.uniform(0.01,0.10),2)
    
    p = 0.5  
    u = round(random.uniform(0.10,0.50),2)
    d = round(random.uniform(0.10,0.50),2)
    

    print("dt=",dt)
    print("S= ", S)
    print("r= ", r)
    print("u= ", u)
    print("d= ", d)
    input("Press Enter to continue...")

    call()

elif Choice == "MC" or Choice == "mc" or Choice == "manual call":

    dt = 2 #input("Enter the timestep: ")
    S = float(input("Enter the initial asset price: "))
    r = float(input("Enter the risk-free discount rate: "))
    p = 0.5 
    u = float(input("Enter the asset growth factor u: "))
    d = float(input("Enter the asset growth factor d: "))
    input("Press Enter to continue...")
    call()

elif Choice == "RP" or Choice == "rp" or Choice == "random put":
    dt = 2  # input("Enter the timestep: ")
    S = round(random.uniform(5,150),0)
    r = round(random.uniform(0.01,0.10),2)
    p = 0.5 
    u = round(random.uniform(0.10,0.50),2)
    d = round(random.uniform(0.10,0.50),2)

    print("dt=",dt)
    print("S= ", S)
    print("r= ", r)
    print("u= ", u)
    print("d= ", d)
    input("Press Enter to continue...")

    put()

elif Choice == "MP" or Choice == "mp" or Choice == "manual put":

    dt = 2 
    S = float(input("Enter the initial asset price: "))
    r = float(input("Enter the risk-free discount rate: "))
    p = 0.5 
    u = float(input("Enter the asset growth factor u: "))
    d = float(input("Enter the asset growth factor d: "))
    input("Press Enter to continue...")

    put()



else:
    print("Not a valid Choice please select another")

    '''
    print(
                                Spp,
                                Cpp,

                Sp,
                Cp,
                hcp,
                                Spn,
                                Cpn,
    S,
    C,
    hc,

                Sn,
                Cn,
                hcn,

                                Snn,
                                Cnn

    )
    '''







