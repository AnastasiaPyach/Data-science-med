from tkinter import *
class TrafficLight(Tk):
    test_count = 0
    running = True
    def __init__(self):
        super().__init__()
        self.title('TrafficLight')
        self.geometry('200x280')
        self.canv = canv = Canvas(self, width=80, height=255, bg='#565656')
        self.one = canv.create_oval(10, 10, 75, 75, outline='black', fill='#c27989', width=2)
        self.two = canv.create_oval(10, 95, 75, 160, outline='black', fill='#eedc82', width=2)
        self.three = canv.create_oval(10, 180, 75, 245, outline='black', fill='#b1d3b1', width=2)
        canv.pack()
        self.after(2000, self.running)
    def running(self):
        self.test_count += 1
        if self.test_count == 1:
            self.canv.itemconfig(self.one, fill='red')
            self.after(7000, self.running)
        elif self.test_count == 2:
            self.canv.itemconfig(self.two, fill='yellow')
            self.canv.itemconfig(self.one, fill='#c27989')
            self.after(2000, self.running)
        elif self.test_count == 3:
            self.canv.itemconfig(self.three, fill='green')
            self.canv.itemconfig(self.two, fill='#eedc82')
            self.after(7000, self.running)
        else:
            self.test_count = 0
            self.canv.itemconfig(self.one, fill='red')
            self.canv.itemconfig(self.three, fill='#b1d3b1')
            self.after(0, self.running)

traffic_light = TrafficLight()
traffic_light.mainloop()