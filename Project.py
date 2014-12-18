from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket2 = drawpad.create_rectangle(415,590,420,595, fill="green")
rocket1 = drawpad.create_rectangle(385,585,390,590, fill="cyan")
player2 = drawpad.create_oval(405,580,425,600, fill="green")
player1 = drawpad.create_oval(375,580,395,600, fill="cyan")
enemyboss = drawpad.create_rectangle(15,50,25,60, fill="purple")
enemyman1 = drawpad.create_rectangle(750,100,800,120, fill="red")
enemyman2 = drawpad.create_rectangle(5,100,50,120, fill="red")
rocket1Fired = False
rocket2Fired = False

direction = 5


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        self.prompt = "Player 1 Rockets :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='cyan')
        self.label1.pack()

        self.rockets = 10
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='cyan')
        self.rocketsTxt.pack()
        
        self.prompt = "Player 2 Rockets :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets2 = 10
        
        self.rockets2Txt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rockets2Txt.pack()
        
        self.rocketFired = False
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemyboss
        global enemyman1
        global enemyman2
        global direction
        global rocket1
        global rocket2
        global rocket1Fired
        global rocket2Fired

        global didWeHit
        didWeHit = self.collisionDetect()
        
        ex1,ey1,ex2,ey2 = drawpad.coords(enemyboss)
        e1x1,e1y1,e1x2,e1y2 = drawpad.coords(enemyman1)
        e2x1,e2y1,e2x2,e2y2 = drawpad.coords(enemyman2)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        r2x1,r2y1,r2x2,r2y2 = drawpad.coords(rocket2)

        p1x1,p1y1,p1x2,p1y2 = drawpad.coords(player1)
        p2x1,p2y1,p2x2,p2y2 = drawpad.coords(player2)

        if ex2 > 800:
            direction = - 5
        elif ex1 < 0:
            direction = 5
        elif didWeHit == True:
            drawpad.delete(enemyboss)
       
        if rocket1Fired == True:
            drawpad.move(rocket1,0,-5)
        if rocket2Fired == True:
            drawpad.move(rocket2,0,-5)        
            
        if ry2 < 0:
            drawpad.move(rocket1,p1x1-rx1+6, p1y1 - ry1 + 6)
            rocket1Fired = False
        if r2y2 < 0:
            drawpad.move(rocket2,p2x1-r2x1+6, p2y1 - r2y1 + 6)
            rocket2Fired = False        
        drawpad.move(enemyboss, direction, 0)
  
        drawpad.after(5,self.animate)

    def key(self,event):
        global player1
        global player2
        global rocket1Fired
        global rocket2Fired
        global rocket1
        global rocket2
        
        p1x1,p1y1,p1x2,p1y2 = drawpad.coords(player1)
        if rocket1Fired == False:
            if event.char == 'e' and self.rockets > 0:
                rocket1Fired = True
                self.rockets = self.rockets - 1
                self.rocketsTxt.configure(text=str(self.rockets))
        elif event.char == 'a' and p1x1 >= 0: 
            drawpad.move(player1,-20,0)
            drawpad.move(rocket1,-20,0)
        elif event.char == 'd' and p1x2 <= drawpad.winfo_width() :
            drawpad.move(player1,20,0)
            drawpad.move(rocket1,20,0)
        elif event.char == 'w' and p1y1 >= 0: 
            drawpad.move(player1,0,-20)
            drawpad.move(rocket1,0,-20)
        elif event.char == 's' and p1y1 >= 0: 
            drawpad.move(player1,0,20)
            drawpad.move(rocket1,0,20)    
    
        p2x1,p2y1,p2x2,p2y2 = drawpad.coords(player2)
        if rocket2Fired == False:
            if event.char == 'u' and self.rockets > 0:
                rocket2Fired = True
                self.rockets2 = self.rockets2 - 1
                self.rockets2Txt.configure(text=str(self.rockets2))
        elif event.char == 'j' and p2x1 >= 0: 
            drawpad.move(player2,-20,0)
            drawpad.move(rocket2,-20,0) 
        elif event.char == 'l' and p2x2 <= drawpad.winfo_width() :
            drawpad.move(player2,20,0)
            drawpad.move(rocket2,20,0)
        elif event.char == 'i' and p2y1 >= 0: 
            drawpad.move(player2,0,-20)
            drawpad.move(rocket2,0,-20)
        elif event.char == 'k' and p2y1 >= 0: 
            drawpad.move(player2,0,20)
            drawpad.move(rocket2,0,20)    
    
    def collisionDetect(self):
        
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemyboss)
        e1x1,e1y1,e1x2,e1y2 = drawpad.coords(enemyman1)
        e2x1,e2y1,e2x2,e2y2 = drawpad.coords(enemyman2)

        if rx1 > ex1 and ry1 < ey2 and rx2 < ex2 and ry2 < ey2:
            return True
        else:
            return False
        if rx1 > e1x1 and ry1 < e1y2 and rx2 < e1x2 and ry2 < e1y2:
            return True
        else:
            return False
        if rx1 > e2x1 and ry1 < e2y2 and rx2 < e2x2 and ry2 < e2y2:
            return True
        else:
            return False
app = myApp(root)
root.mainloop()