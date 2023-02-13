from operator import truediv
from pickle import FALSE, TRUE
from tty import IFLAG
from datetime import*


def arithmetic (arv1:float,tehe:str,arv2:float)->any:
    """Haarme arithmetic.
    :parem int a,b: Järjend arithmetic numbridest
    irtype: str
    """
    if tehe=="+":
       vastus=arv1+arv2
    elif tehe=="-":
       vastus=arv1+arv2
    elif tehe=="*":
        vastus=arv1+arv2
    elif tehe=="/":
        if arv2==0:
           vsatus="DIV0"
        else:
            vastus=arv1/arv2
    else:
        vastus="Tundmatu tehe"

    return vastus


def is_year_leap(aasta: int)->bool:
    """Haarme is_year_leap
    """
    if aasta%4!=0:
        t=True
    else:
        t=False 

    return


   
def square(tehe:float)->any:
    """
    Määrme square
    :parem tehe a2: Järjend square numbridest
    :rtype: str
    """
    a = tehe * 4
    b = tehe**2
    c = (tehe * 1.414)//1
    return a,b,c



def season(m:int)->str:
    """
    Määrme season
    :parem int m: Järjend season numbridest
    :rtype: str
    """
    if  m in (12,1,2):
        vas= "talv"
    elif m in (3,4,5):
        vas="kevad"
    elif m in (6,7,8):
        vas="suvi"
    elif m in (9,10,11):
        vas="sügis"
    else:
        vas="Viga"
    return vas


def bank(b:float,aa:int)->float:
    """Param float: Järjend
    : rtype: float
    """
    for i in range(aa):
        b=b+b*0.1
    return


def is_prime(arv:int)->bool:
    """
    Määrme is_prime
    :parem int arv: Järjend is_prime numbridest
    :rtype: bool
    """
    flag= True
    for i in range(2,arv):
        if arv%i==0:
            flag= False
            break
    return flag


def date_(d: int, m: int, y: int)-> bool:
    """Määrme date
    """
    try:
        print(date(y,m,d))
        flag=True
    except :
        print("Viga")
        flag=False 
    return flag


   
