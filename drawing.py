#drawing functions: horizontal buttons, vertical buttons

def drawHorizontalButton(canvas,data,cx,cy,text=""):
    canvas.create_rectangle(cx-45,cy-20,cx+45,cy+20,
                            fill="#99E6FF",outline="#99E6FF")
    canvas.create_oval(cx-65,cy-20,cx-25,cy+20,fill="#99E6FF",outline="#99E6FF")
    canvas.create_oval(cx+25,cy-20,cx+65,cy+20,fill="#99E6FF",outline="#99E6FF")
    canvas.create_text(cx,cy,text=text,font=("perpetua","16"),fill="white",activefill="red")

def drawVerticalButton(canvas,data,cx,cy,text=""):
    canvas.create_rectangle(cx-20,cy-25,cx+20,cy+25,
                            fill="#99E6FF",outline="#99E6FF")
    canvas.create_oval(cx-20,cy-45,cx+20,cy-5,fill="#99E6FF",outline="#99E6FF")
    canvas.create_oval(cx-20,cy+5,cx+20,cy+45,fill="#99E6FF",outline="#99E6FF")
    canvas.create_text(cx,cy,text=text,font=("perpetua","14"),fill="white",activefill="gray")
    canvas.create_polygon(cx,cy+38,cx-8,cy+23,cx+8,cy+23,fill="white",activefill="red")
    canvas.create_polygon(cx,cy-38,cx-8,cy-23,cx+8,cy-23,fill="white",activefill="red")

def drawLargeHorizontalButton(canvas,data,cx,cy,text=""):
    canvas.create_rectangle(cx-80,cy-40,cx+80,cy+40,
                            fill="#99E6FF",outline="#99E6FF")
    canvas.create_oval(cx-115,cy-40,cx-45,cy+40,fill="#99E6FF",outline="#99E6FF")
    canvas.create_oval(cx+45,cy-40,cx+115,cy+40,fill="#99E6FF",outline="#99E6FF")
    canvas.create_text(cx,cy,text=text,font=("perpetua","24"),fill="white",activefill="red")

def drawRiver(canvas,data):
    if data.drawFlop == True:
        data.river[0].drawCard(canvas,data.width//2,data.height//2,data)
        data.river[1].drawCard(canvas,data.width//2-100,data.height//2,data)
        data.river[2].drawCard(canvas,data.width//2+100,data.height//2,data)
    if data.drawTurn == True:
        data.river[3].drawCard(canvas,data.width//2+200,data.height//2,data)
    if data.drawRiver == True:
        data.river[4].drawCard(canvas,data.width//2+300,data.height//2,data)

def drawGameScreen(canvas,data):
    drawTable(canvas,data)
    drawVerticalButton(canvas,data,data.width//2,
                           data.height-100,text=data.currentBet)
    drawHorizontalButton(canvas,data,data.width//2+100,
                             data.height-100,text="Raise")
    drawHorizontalButton(canvas,data,data.width//2+240,
                            data.height-100,text="Call")
    drawHorizontalButton(canvas,data,data.width//2+380,
                             data.height-100,text="Check")
    drawHorizontalButton(canvas,data,data.width//2-100,data.height-100,text="Fold")
    p = data.players[0]
    if p.status == "player":
        p.drawPlayerCards(canvas,data.width//2,data.height-203,data)
    drawAICards(canvas,data)
    drawRiver(canvas,data)
    canvas.create_text(300,data.height-100,font=("Perpetua","24"),
                       fill="white",text="Your Money: $"+str(data.players[0].money))
    canvas.create_text(data.width//2,400,font=("Perpetua","24"),
                       fill="white",text="Current Pot: $"+str(data.pot))

def drawAICards(canvas,data):
    if data.players[1].drawCards and not data.players[1].revealCards:
        data.players[1].drawPlayerCardBacks(canvas,data.width//2-400,data.height-203,data)
    elif data.players[1].drawCards and data.players[1].revealCards:
        data.players[1].drawPlayerCardBacks(canvas,data.width//2-400,data.height-203,data)
    canvas.create_text(data.width//2-400,data.height-260,fill="white",
                       font=("Perpetua","18"),text="$"+str(data.players[1].money))
    canvas.create_text(data.width//2-400,data.height-280,fill="white",
                       font=("Perpetua","18"),text=data.players[1].lastMove)
    if data.players[2].drawCards and not data.players[2].revealCards:
        data.players[2].drawPlayerCardBacks(canvas,data.width//2-600,data.height//2,data)
    elif data.players[2].drawCards and data.players[2].revealCards:
        data.players[2].drawPlayerCardBacks(canvas,data.width//2-600,data.height//2,data)
    canvas.create_text(data.width//2-800,data.height//2,fill="white",
                       font=("Perpetua","18"),text="$"+str(data.players[2].money))
    canvas.create_text(data.width//2-800,data.height//2+20,fill="white",
                       font=("Perpetua","18"),text=data.players[2].lastMove)
    if data.players[3].drawCards and not data.players[3].revealCards:
        data.players[3].drawPlayerCardBacks(canvas,data.width//2-400,203,data)
    elif data.players[3].drawCards and data.players[3].revealCards:
        data.players[3].drawPlayerCardBacks(canvas,data.width//2-400,203,data)
    canvas.create_text(data.width//2-400,100,fill="white",
                       font=("Perpetua","18"),text="$"+str(data.players[3].money))
    canvas.create_text(data.width//2-400,120,fill="white",
                       font=("Perpetua","18"),text=data.players[3].lastMove)
    if data.players[4].drawCards and not data.players[4].revealCards:
        data.players[4].drawPlayerCardBacks(canvas,data.width//2,203,data)
    elif data.players[4].drawCards and data.players[4].revealCards:
        data.players[4].drawPlayerCardBacks(canvas,data.width//2,203,data)
    canvas.create_text(data.width//2,100,fill="white",
                       font=("Perpetua","18"),text="$"+str(data.players[4].money))
    canvas.create_text(data.width//2,120,fill="white",
                       font=("Perpetua","18"),text=data.players[4].lastMove)
    if data.players[5].drawCards and not data.players[5].revealCards:
        data.players[5].drawPlayerCardBacks(canvas,data.width//2+400,203,data)
    elif data.players[5].drawCards and data.players[5].revealCards:
        data.players[5].drawPlayerCardBacks(canvas,data.width//2+400,203,data)
    canvas.create_text(data.width//2+400,100,fill="white",
                       font=("Perpetua","18"),text="$"+str(data.players[5].money))
    canvas.create_text(data.width//2+400,120,fill="white",
                       font=("Perpetua","18"),text=data.players[5].lastMove)
    if data.players[6].drawCards and not data.players[6].revealCards:
        data.players[6].drawPlayerCardBacks(canvas,data.width//2+600,data.height//2,data)
    elif data.players[6].drawCards and data.players[6].revealCards:
        data.players[6].drawPlayerCardBacks(canvas,data.width//2+600,data.height//2,data)
    canvas.create_text(data.width//2+800,data.height//2,fill="white",
                       font=("Perpetua","18"),text="$"+str(data.players[6].money))
    canvas.create_text(data.width//2+800,data.height//2+20,fill="white",
                       font=("Perpetua","18"),text=data.players[6].lastMove)
    if data.players[7].drawCards and not data.players[7].revealCards:
        data.players[7].drawPlayerCardBacks(canvas,data.width//2+400,data.height-203,data)
    elif data.players[7].drawCards and data.players[7].revealCards:
        data.players[7].drawPlayerCardBacks(canvas,data.width//2+400,data.height-203,data)
    canvas.create_text(data.width//2+400,data.height-260,fill="white",
                       font=("Perpetua","18"),text="$"+str(data.players[7].money))
    canvas.create_text(data.width//2+400,data.height-280,fill="white",
                       font=("Perpetua","18"),text=data.players[7].lastMove)



def drawTable(canvas,data):
    #draws green table
    cx = data.width//2
    cy = data.height//2
    h = 700
    w = 800
    canvas.create_rectangle(0,0,data.width+50,data.height+50,fill="#FF6666")
    canvas.create_rectangle(cx-w//2,cy-h//2,cx+w//2,cy+h//2,
                            outline="#008000",fill="#008000")
    canvas.create_oval(cx-w//2-h//2,cy-h//2,cx-w//2+h//2,cy+h//2,
                       outline="#008000", fill="#008000")
    canvas.create_oval(cx+w//2-h//2,cy-h//2,cx+w//2+h//2,cy+h//2,
                       outline="#008000", fill="#008000")

def drawSplashScreen(canvas,data):
    canvas.create_rectangle(0,0,data.width+50,data.height+50,fill="#FF6666")
    canvas.create_text(data.width//2,100,text="Texas Hold'Em",fill="white",font=("Perpetua","100"))
    drawLargeHorizontalButton(canvas,data,data.width//3,data.height//2,text="Play")
    drawLargeHorizontalButton(canvas,data,data.width*2//3,data.height//2,text="Rules")

def drawHelpScreen(canvas,data):
    canvas.create_rectangle(0,0,data.width+50,data.height+50,fill="#FF6666")
    canvas.create_text(data.width//2,100,font=("Perpetua","100"),text="Texas Hold'Em",fill="white")
    canvas.create_text(data.width//2,200,font=("Perpetua","36"),text="Rules",fill="white")
    canvas.create_text(data.width//2,550,font=("Perpetua","24"),fill="white",
                       text=data.helpText)
    drawHorizontalButton(canvas,data, data.width-100,50,text="to game >")
