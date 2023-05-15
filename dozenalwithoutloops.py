import math
intDec=int(input("Please enter a decimal number:"))
boolNeg=False
if intDec<0:
	boolNeg=True
	intDec=abs(intDec)
while intDec>=5159780352:
	intDec=int(input("Too large. Enter another"))
intNine=intDec/12**9
if intNine>=1:
	intNn=(math.floor(intNine))
	intDec=intDec-(intNn*(12**9))
	if intNn==11:
		intNn="E"
	elif intNn==10:
		intNn="X"
else:
	intNn=0
intEight=intDec/12**8
if intEight>=1:
	intEg=(math.floor(intEight))
	intDec=intDec-(intEg*(12**8))
	if intEg==11:
		intEg="E"
	elif intEg==10:
		intEg="X"
else:
	intEg=0
intSeven=intDec/12**7
if intSeven>=1:
	intSv=(math.floor(intSeven))
	intDec=intDec-(intSv*(12**7))
	if intSv==11:
		intSv="E"
	elif intSv==10:
		intSv="X"
else:
	intSv=0
intSix=intDec/12**6
if intSix>=1:
	intSx=(math.floor(intSix))
	intDec=intDec-(intSx*(12**6))
	if intSx==11:
		intSx="E"
	elif intSx==10:
		intSx="X"
else:
	intSx=0
intFive=intDec/12**5
if intFive>=1:
	intFv=(math.floor(intFive))
	intDec=intDec-(intFv*(12**5))
	if intFv==11:
		intFv="E"
	elif intFv==10:
		intFv="X"
else:
	intFv=0
intFour=intDec/12**4
if intFour>=1:
	intFu=(math.floor(intFour))
	intDec=intDec-(intFu*(12**4))
	if intFu==11:
		intFu="E"
	elif intFu==10:
		intFu="X"
else:
	intFu=0
intThree=intDec/12**3
if intThree>=1:
	intTr=(math.floor(intThree))
	intDec=intDec-(intTr*(12**3))
	if intTr==11:
		intTr="E"
	elif intTr==10:
		intTr="X"
else:
	intTr=0
intTwo=intDec/12**2
if intTwo>=1:
	intTo=(math.floor(intTwo))
	intDec=intDec-(intTo*(12**2))
	if intTo==11:
		intTo="E"
	elif intTo==10:
		intTo="X"
else:
	intTo=0
intOne=intDec/12
if intOne>=1:
	intOe=(math.floor(intOne))
	intDec=intDec-(intOe*(12))
	if intOe==11:
		intOe="E"
	elif intOe==10:
		intOe="X"
else:
	intOe=0
if intDec==11:
	intDec="E"
elif intDec==10:
	intDec="X"
if boolNeg:
	  if not intNn==0:
		  strDoz=("-"+str(intNn)+str(intEg)+str(intSv)+str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	  elif not intEg==0:
		  strDoz=("-"+str(intEg)+str(intSv)+str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	  elif intSv!=0:
		  strDoz=("-"+str(intSv)+str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	  elif intSx!=0:
		  strDoz=("-"+str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	  elif intFv!=0:
		  strDoz=("-"+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	  elif intFu!=0:
	      strDoz=("-"+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	  elif intTr!=0:
	      strDoz=("-"+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	  elif intTo!=0:
	      strDoz=("-"+str(intTo)+str(intOe)+str(intDec))
	  elif intOe!=0:
	      strDoz=("-"+str(intOe)+str(intDec))
	  else:
	       strDoz=str("-"+intDec)
else:
	if not intNn==0:
		strDoz=(str(intNn)+str(intEg)+str(intSv)+str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	elif not intEg==0:
		strDoz=(str(intEg)+str(intSv)+str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	elif intSv!=0:
		strDoz=(str(intSv)+str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	elif intSx!=0:
		strDoz=(str(intSx)+str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	elif intFv!=0:
		strDoz=(str(intFv)+str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	elif intFu!=0:
	    strDoz=(str(intFu)+str(intTr)+str(intTo)+str(intOe)+str(intDec))
	elif intTr!=0:
	    strDoz=(str(intTr)+str(intTo)+str(intOe)+str(intDec))
	elif intTo!=0:
	    strDoz=(str(intTo)+str(intOe)+str(intDec))
	elif intOe!=0:
	    strDoz=(str(intOe)+str(intDec))
	else:
	     strDoz=str(intDec)
print("In dozenal that is "+strDoz+".")
