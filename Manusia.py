class Manusia:
    # class attribute
    SUKU = "bugis"
    
    def __init__(self,name,age,agama,jnskel,alamat,status):
       self.name    = name
       self.age     = age
       self.jnskel  = jnskel
       self.agama   = agama
       self.alamat  = alamat
       self.status  = status
      
    def biodata(self):
       #return f"{self.name} is {self.age} years old"
       return f"Nama: {self.name} \nUsia: {self.age} \nAgama: {self.agama} \nJenis Kelamin: {self.jnskel} \nAlamat: {self.alamat} \nStatus: {self.status}"
      
 tes_masusia = Masusia("ageng",22,"Agama","Laki-laki","Batang","jomblo")
 print(tes_manusia.biodata())
 print("Suku: ",tes_manusia.SUKU)
