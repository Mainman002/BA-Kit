from bge import logic
path = logic.expandPath("//")

def save():
    cont = logic.getCurrentController()
    own = cont.owner 
    # 'info' is what will be saved to the file.
    # Example:
    # info = str(*What you want to save*)
    
    info = str(own['score']) + " , " + str(own['L1']) + " , " + str(own['L2']) + " , " + str(own['L3']) + " , " + str(own['L4']) + " , " + str(own['L5']) + " , " + str(own['L6']) + " , " + str(own['L7']) + " , " + str(own['L8']) + " , " + str(own['L9']) + " , " + str(own['L10']) + " , " + str(own['L11']) + " , " + str(own['L12']) + " , " + str(own['L13']) + " , " + str(own['L14']) + " , " + str(own['L15']) + " , " + str(own['L16']) + " , " + str(own['L17']) + " , " + str(own['L18']) + " , " + str(own['L19']) + " , " + str(own['L20']) + " , " + str(own['L21']) + " , " + str(own['L22']) + " , " + str(own['L23']) + " , " + str(own['L24']) + " , " + str(own['L25']) + " , " + str(own['L26']) + " , " + str(own['L27']) + " , " + str(own['L28']) + " , " + str(own['L29']) + " , " + str(own['L30']) + " , " + str(own['L31']) + " , " + str(own['L32']) + " , " + str(own['L33']) + " , " + str(own['L34']) + " , " + str(own['L35']) + " , " + str(own['L36']) + " , " + str(own['L37']) + " , " + str(own['L38']) + " , " + str(own['L39']) + " , " + str(own['L40']) + " , " + str(own['L41']) + " , " + str(own['L42']) + " , " + str(own['L43']) + " , " + str(own['L44']) + " , " + str(own['L45']) + " , " + str(own['L46']) + " , " + str(own['L47']) + " , " + str(own['L48']) + " , " + str(own['L49']) + " , " + str(own['L50'])
        
    file = open(path+".#scorekeep1empty1.txt", 'w')    
    file.write(str(info))
    
def saveTemp():
    cont = logic.getCurrentController()
    own = cont.owner 
    # 'info' is what will be saved to the file.
    # Example:
    # info = str(*What you want to save*)
    
    info = str(own['score'])
        
    file = open(path+".#Temp.txt", 'w')    
    file.write(str(info))
    
    
def loadTemp():
    cont = logic.getCurrentController()
    own = cont.owner
    
    file = open(path+'.#Temp.txt','r')
    line = file.readline().replace('\n','').split(',')
    own['score'] = int(line[0])
    
    
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
    own['L5'] = int(line[5])
    own['L6'] = int(line[6])
    own['L7'] = int(line[7])
    own['L8'] = int(line[8])
    own['L9'] = int(line[9])
    own['L10'] = int(line[10])
    own['L11'] = int(line[11])
    own['L12'] = int(line[12])
    own['L13'] = int(line[13])
    own['L14'] = int(line[14])
    own['L15'] = int(line[15])
    own['L16'] = int(line[16])
    own['L17'] = int(line[17])
    own['L18'] = int(line[18])
    own['L19'] = int(line[19])
    own['L20'] = int(line[20])
    own['L21'] = int(line[21])
    own['L22'] = int(line[22])
    own['L23'] = int(line[23])
    own['L24'] = int(line[24])
    own['L25'] = int(line[25])
    own['L26'] = int(line[26])
    own['L27'] = int(line[27])
    own['L28'] = int(line[28])
    own['L29'] = int(line[29])
    own['L30'] = int(line[30])
    own['L31'] = int(line[31])
    own['L32'] = int(line[32])
    own['L33'] = int(line[33])
    own['L34'] = int(line[34])
    own['L35'] = int(line[35])
    own['L36'] = int(line[36])
    own['L37'] = int(line[37])
    own['L38'] = int(line[38])
    own['L39'] = int(line[39])
    own['L40'] = int(line[40])
    own['L41'] = int(line[41])
    own['L42'] = int(line[42])
    own['L43'] = int(line[43])
    own['L44'] = int(line[44])
    own['L45'] = int(line[45])
    own['L46'] = int(line[46])
    own['L47'] = int(line[47])
    own['L48'] = int(line[48])
    own['L49'] = int(line[49])
    own['L50'] = int(line[50])
