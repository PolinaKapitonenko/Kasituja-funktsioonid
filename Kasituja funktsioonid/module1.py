from pickle import TRUE


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
    """
    """
    if aasta%4!=0:
        t=True
    else:
        t=False 

    return


   