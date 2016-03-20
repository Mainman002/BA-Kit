from bge import logic
path = logic.expandPath("//levels/")

def save():
    cont = logic.getCurrentController()
    own = cont.owner 
    # 'info' is what will be saved to the file.
    # Example:
    # info = str(*What you want to save*)
    
    info = str(own['score']) + " , " + str(own['L1']) + " , " + str(own['L2']) + " , " + str(own['L3']) + " , " + str(own['L4']) + " , " + str(own['L5']) + " , " + str(own['L6']) + " , " + str(own['L7']) + " , " + str(own['L8']) + " , " + str(own['L9']) + " , " + str(own['L10']) + " , " + str(own['L11']) + " , " + str(own['L12']) + " , " + str(own['L13']) + " , " + str(own['L14']) + " , " + str(own['L15']) + " , " + str(own['L16']) + " , " + str(own['L17']) + " , " + str(own['L18']) + " , " + str(own['L19']) + " , " + str(own['L20']) + " , " + str(own['L21']) + " , " + str(own['L22']) + " , " + str(own['L23']) + " , " + str(own['L24']) + " , " + str(own['L25']) + " , " + str(own['L26']) + " , " + str(own['L27']) + " , " + str(own['L28']) + " , " + str(own['L29']) + " , " + str(own['L30']) + " , " + str(own['L31']) + " , " + str(own['L32']) + " , " + str(own['L33']) + " , " + str(own['L34']) + " , " + str(own['L35'])
        
    file = open(path+".#scorekeep1empty1.txt", 'w')    
    file.write(str(info))
    
def load():
    cont = logic.getCurrentController()
    own = cont.owner
    
    file = open(path+'.#scorekeep1empty1.txt','r')
    line = file.readline().replace('\n','').split(',')
    own['score'] = int(line[0])
    own['L1'] = int(line[1])
    own['L2'] = int(line[2])
    own['L3'] = int(line[3])
    own['L4'] = int(line[4])
    own['L5'] = int(line[1])
    own['L6'] = int(line[2])
    own['L7'] = int(line[3])
    own['L8'] = int(line[4])
    own['L9'] = int(line[1])
    own['L10'] = int(line[2])
    own['L11'] = int(line[3])
    own['L12'] = int(line[4])
    own['L13'] = int(line[1])
    own['L14'] = int(line[2])
    own['L15'] = int(line[3])
    own['L16'] = int(line[4])
    own['L17'] = int(line[1])
    own['L18'] = int(line[2])
    own['L19'] = int(line[3])
    own['L20'] = int(line[4])
    own['L21'] = int(line[1])
    own['L22'] = int(line[2])
    own['L23'] = int(line[3])
    own['L24'] = int(line[4])
    own['L25'] = int(line[1])
    own['L26'] = int(line[2])
    own['L27'] = int(line[3])
    own['L28'] = int(line[4])
    own['L29'] = int(line[1])
    own['L30'] = int(line[2])
    own['L31'] = int(line[3])
    own['L32'] = int(line[4])
    own['L33'] = int(line[1])
    own['L34'] = int(line[2])
    own['L35'] = int(line[3])