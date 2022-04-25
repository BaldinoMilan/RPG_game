import création_perso as crea 

class capacity:
    def __init__(self, name, ammount, target, PV = False, PVB = False, PAT = False, PATB = False, PDEF = False, empty = None, more = False, less = False):
        self.name = name
        self.ammount = ammount
        self.target = crea.character(target)
        self.change_PV = PV 
        self.change_PVB = PVB 
        self.change_PAT = PAT 
        self.change_PATB = PATB 
        self.change_PDEF = PDEF
        self.empty = empty
        self.more = more 
        self.less = less 
        liste = [self.change_PV, self.change_PVB, self.change_PAT, self.change_PATB, self.change_PDEF]
        if True in list:
            counting = list.count(True)        
            self.empty = liste.index("True")
                
            if self.more == True:
                if self.empty == liste[0]:
                    crea.target.PV += self.ammount
                    
                elif self.empty == liste[1]:
                    crea.target.PVB += self.ammount
                    
                elif self.empty == liste[2]:
                    crea.target.PAT += self.ammount 
                    
                elif self.empty == liste[3]:
                    crea.target.PATB += self.ammount
                    
                elif self.empty == liste[4]:
                    crea.target.PDEF += self.ammount
                    
            elif self.less == True:
                self.ammount = -self.ammount 
                if self.empty == liste[0]:
                    crea.target.PV += self.ammount
                    
                elif self.empty == liste[1]:
                    crea.target.PVB += self.ammount
                    
                elif self.empty == liste[2]:
                    crea.target.PAT += self.ammount 
                    
                elif self.empty == liste[3]:
                    crea.target.PATB += self.ammount
                    
                elif self.empty == liste[4]:
                    crea.target.PDEF += self.ammount