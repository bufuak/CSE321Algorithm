def hanoirecur(n, SRC, AUX, DST,time):
    if n > 0:       
        hanoirecur(n - 1, SRC, DST, AUX,time) # n-1 elemanı sourceden auxa taşı
        disk = SRC[0].pop() # n. elemanı sourceden al
        print ("Disk " + str(disk) + ": " + SRC[1] + " to " + DST[1])
        time[disk-1]+=abs(DST[2]-SRC[2])*disk # n. eleman için geçecek süreyi hesapla
        DST[0].append(disk)  # n. elemanı deste koy
        hanoirecur(n - 1, AUX, SRC, DST,time) # kalan n-1 diski auxtan deste taşı
        
def hanoi(n):
  # Çubukları ayarla
  SRC = ([], "SRC",1) # Her çubuğun bir uzaklık birimi var
  AUX = ([], "AUX",2)
  DST = ([], "DST",3)
  time=[]
  for num in reversed(range(1,n+1)):
    SRC[0].append(num)  # source çubuğunu diskler ile doldur
    time.append(0)      # zamanı ise 0 lar ile
  # SRC[0] şu anda diskler ile dolu [5,4,3,2,1] gibi

  hanoirecur(n,SRC,AUX,DST,time) 
   # SRC[0] şu anda hiçbir diske sahip değil
   # DST[0] çubuğu src'deki diskler ile dolu

  for disk in range(1,n+1):
   print ("Elapsed time for disk "+str(disk)+": "+str(time[disk-1]))
  
hanoi(3)