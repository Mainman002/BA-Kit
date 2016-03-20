import bge

from bge import render

fullscreen = False

def main():
    
    cont = bge.logic.getCurrentController()
    own = cont.owner

    f12key = cont.sensors['F12K']
    moaFullscreen = cont.sensors['MOAFullscreen']
    mouseL = cont.sensors['MouseL']

    if f12key.positive:
        if render.getFullScreen() == False:
            render.setFullScreen(True)
        else:
            render.setFullScreen(False)
            
    if moaFullscreen.positive:
        if mouseL.positive:
            if render.getFullScreen() == False:
                render.setFullScreen(True)
            else:
                render.setFullScreen(False)
    
main()