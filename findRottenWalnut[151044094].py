def compareScales (leftScaleList, rightScaleList):
 result = sum(leftScaleList) - sum(rightScaleList)
 if result < 0:
  return 1
 elif result > 0:
  return -1
 else:
  return 0
 
def findRottenWalnut(givenList):
  return findRottenWalnutrecur(givenList,0,len(givenList))
  
def findRottenWalnutrecur(givenList,start,end):
  middle=int((start+end)/2)
  if  len(givenList[start:end])%2==0: # Kalan liste çiftse
    whichList=compareScales(givenList[start:middle],givenList[middle:end]) # İki listeyi karşılaştır
    if whichList==0:  # Eğer iki liste eşitse çürük yoktur -1 döndür
      return -1
    elif whichList<0: # Sağdaki liste daha büyükse start'ı middle yap o listeyi araştır
      start=middle
      return findRottenWalnutrecur(givenList,start,end)
    else:             # Soldaki liste daha büyükse end'i middle yap o listeyi araştır
      end=middle
      return findRottenWalnutrecur(givenList,start,end)
      
  else:                              # Kalan liste tekse
    if len(givenList[start:end])==1: # Tek elemanlı bir liste kalmışsa
      if givenList[middle]!=givenList[0] or givenList[middle]!=givenList[1]: # Ve bu eleman 0 ya da 1. indexteki elemanlara eşit değilse
        return middle                # Çürüktür indexi döndür
      else:
        return -1                    # Eşitse listede çürük yoktur -1 döndür
    else:
      if givenList[middle]>givenList[middle+1]:   # Kalan listenin ortadaki elemanı bi sonrakinden büyükse
        return middle+1                           # Bi sonraki çürüktür
      elif givenList[middle]>givenList[middle-1]: # Kalan listenin ortadaki elemanı bi öncekinden büyükse
        return middle-1                           # Bi önceki çürüktür
      elif givenList[middle]<givenList[middle-1]: # Kalan listenin ortadaki elemanı bi öncekinden küçükse
        return middle                             # Ortadaki çürüktür
                                                  # Hiçbiri olmadıysa listeyi tekrar böl ama ortadaki elemanı listelere katma
      whichList=compareScales(givenList[start:middle],givenList[middle+1:end])
      if whichList==0:                            # Listeler eşitse
        return -1
      elif whichList<0:
        start=middle+1
        return findRottenWalnutrecur(givenList,start,end)
      else:
        end=middle
        return findRottenWalnutrecur(givenList,start,end)
        

def testFindRottenWalnut(n):
  exList =[]
  for i in range(0,n+1):
    exList.append(1)
  print ("Lenght of next test list is: "+str(len(exList)))
  print (exList)
  index=findRottenWalnut(exList)
  print ("Founded rotten walnut in: "+str(index))
  
  for num in range(0,len(exList)):
    exList[num]=0
    print (exList)
    index=findRottenWalnut(exList)
    exList[num]=1
    print ("Founded rotten walnut in: "+str(index))
  
for i in range(8,12):
  testFindRottenWalnut(i)  
 
