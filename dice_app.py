import customtkinter as ctk
import tkinter as tk
from dice import Dice


FONT = ('Times New Roman', 30)

class DiceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Dice Application')
        self._geo(400, 200)

        self.varDice = ctk.StringVar(value='# of Dices')
        self.varSide = ctk.StringVar(value='# of Sides')
        self.varLastRoll = ctk.StringVar(value='Result')

        mainFrame = ctk.CTkFrame(self)
        mainFrame.rowconfigure((0,1,2), weight=1, uniform='a')
        mainFrame.columnconfigure((0,1), weight=1, uniform='a')
        mainFrame.pack(fill='both', expand=True)

        txtDices = ctk.CTkEntry(mainFrame, font=FONT, placeholder_text='# of Dices', justify='center', textvariable=self.varDice)
        txtDices.grid(row=0, column=0, sticky='news')

        txtSides = ctk.CTkEntry(mainFrame, font=FONT, placeholder_text='# of Sides', justify='center', textvariable=self.varSide)
        txtSides.grid(row=0, column=1, sticky='news')

        btnRoll = ctk.CTkButton(mainFrame, text='Roll', font=FONT, command=self.roll_dices)
        btnRoll.grid(row=1, column=0, columnspan=2, sticky='news')

        lblRolls = tk.Label(mainFrame, font=FONT, textvariable=self.varLastRoll)
        lblRolls.grid(row=2, column=0, columnspan=2, sticky='news')

        self.bind('<Shift-Escape>', quit)
        self.mainloop()
    
    def _geo(self, x, y):
        pWidth = x
        pHeight = y
        sWidth = self.winfo_screenwidth()
        sHeight = self.winfo_screenheight()
        mWidth = sWidth//2 - pWidth//2
        mHeight = sHeight//2 - pHeight//2

        self.geometry(f'{pWidth}x{pHeight}+{mWidth}+{mHeight}')

    def roll_dices(self):
        try:
            numOfDices = int(self.varDice.get())
        except:
            numOfDices = 0
        
        try:
            numOfSides = int(self.varSide.get())
        except:
            numOfSides = 0

        if numOfDices == 0:
            self.varLastRoll.set('No Dices to Roll')
        elif numOfSides == 0:
            self.varLastRoll.set('No Sides on Dices')
        else:
            dice = Dice(numOfDices, numOfSides)
            dice.roll()
            self.varLastRoll.set(dice.__repr__())

if __name__ == '__main__':
    g = DiceApp()