################  pause the Sound Actuator

# import bge module
import bge

# get the controller
cont = bge.logic.getCurrentController()

# get the actuator attached to the controller
# my actuator is named Song
act = cont.actuators["Sound"]

# pause the Sound Actuator
act.pauseSound()