from bge import logic
path = logic.expandPath("//")

def save():
    cont = logic.getCurrentController()
    own = cont.owner 
    # 'info' is what will be saved to the file.
    # Example:
    # info = str(*What you want to save*)
    
    info = str(own['score']) + " , " + str(own['level1']) + " , " + str(own['level2'])+ " , " + str(own['level3'])+ " , " + str(own['level4'])+ " , " + str(own['level5'])+ " , " + str(own['level6'])+ " , " + str(own['level7'])+ " , " + str(own['level8'])+ " , " + str(own['level9'])+ " , " + str(own['level10'])+ " , " + str(own['level11'])+ " , " + str(own['level12'])+ " , " + str(own['level13'])+ " , " + str(own['level14'])+ " , " + str(own['level15'])+ " , " + str(own['level16'])+ " , " + str(own['level17'])+ " , " + str(own['level18'])+ " , " + str(own['level19'])+ " , " + str(own['level20'])+ " , " + str(own['level21'])+ " , " + str(own['level22'])+ " , " + str(own['level23'])+ " , " + str(own['level24'])+ " , " + str(own['level25'])+ " , " + str(own['level26'])+ " , " + str(own['level27'])+ " , " + str(own['level28'])+ " , " + str(own['level29'])+ " , " + str(own['level30'])+ " , " + str(own['level31'])+ " , " + str(own['sounds'])+ " , " + str(own['music'])+ " , " + str(own['fullscreen'])
        
    file = open(path+str(own)+".txt", 'w')    
    file.write(str(info))
    
    
def load():
    cont = logic.getCurrentController()
    own = cont.owner
    
    file = open(path+str(own)+'.txt','r')
    line = file.readline().replace('\n','').split(',')
    own['score'] = int(line[0])
    own['level1'] = int(line[1])
    own['level2'] = int(line[2])
    own['level3'] = int(line[3])
    own['level4'] = int(line[4])
    own['level5'] = int(line[5])
    own['level6'] = int(line[6])
    own['level7'] = int(line[7])
    own['level8'] = int(line[8])
    own['level9'] = int(line[9])
    own['level10'] = int(line[10])
    own['level11'] = int(line[11])
    own['level12'] = int(line[12])
    own['level13'] = int(line[13])
    own['level14'] = int(line[14])
    own['level15'] = int(line[15])
    own['level16'] = int(line[16])
    own['level17'] = int(line[17])
    own['level18'] = int(line[18])
    own['level19'] = int(line[19])
    own['level20'] = int(line[20])
    own['level21'] = int(line[21])
    own['level22'] = int(line[22])
    own['level23'] = int(line[23])
    own['level24'] = int(line[24])
    own['level25'] = int(line[25])
    own['level26'] = int(line[26])
    own['level27'] = int(line[27])
    own['level28'] = int(line[28])
    own['level29'] = int(line[29])
    own['level30'] = int(line[30])
    own['level31'] = int(line[31])
    own['sounds'] = int(line[32])
    own['music'] = int(line[33])
    own['fullscreen'] = int(line[34])
   
    
