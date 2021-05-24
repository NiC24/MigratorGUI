__scripter__ = 'nihal.c'
from tkinter import *
import requests

class myFrame(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.parent.title('Script Migrator v1.a')
    
        inp_frame = Frame(relief=RAISED)
        inp_frame.pack()
        inp_frame.columnconfigure([0,1,2,3,4], minsize=50, weight=1)

        inp_frame2 = Frame()
        inp_frame2.pack()
        inp_frame2.columnconfigure([0, 1, 2], minsize=50, weight=1)


        self.inp_cluster = IntVar(value=0)
        self.out_cluster = {'UAT':IntVar(value=0), 'HP':IntVar(value=1), 'HP2':IntVar(value=1), 'HP3':IntVar(value=1)}
        

        lbl_scriptname = Label(master=inp_frame,text="Name of script to be migrated:", anchor=E)
        self.txt_scriptname = Entry(master=inp_frame,width=50)
        
        lbl_inp_cluster = Label(master=inp_frame, text="From:")
        rdio_uat_inp = Radiobutton(master=inp_frame, text="UAT", variable=self.inp_cluster, value=0, state=DISABLED)
        rdio_hp1_inp = Radiobutton(master=inp_frame, text="HP", variable=self.inp_cluster, value=1, state=DISABLED)
        rdio_hp2_inp = Radiobutton(master=inp_frame, text="HP-2", variable=self.inp_cluster, value=2, state=DISABLED)
        rdio_hp3_inp = Radiobutton(master=inp_frame, text="HP-3", variable=self.inp_cluster, value=3, state=DISABLED)
        

        lbl_out_cluster = Label(master=inp_frame, text="To:")
        cbox_uat_out = Checkbutton(master=inp_frame, text="UAT", state=DISABLED, variable=self.out_cluster['UAT'])
        cbox_hp1_out = Checkbutton(master=inp_frame, text="HP", state=DISABLED, variable=self.out_cluster['HP'])
        cbox_hp2_out = Checkbutton(master=inp_frame, text="HP-2", state=DISABLED, variable=self.out_cluster['HP2'])
        cbox_hp3_out = Checkbutton(master=inp_frame, text="HP-3", state=DISABLED, variable=self.out_cluster['HP3'])
        
        self.btn_migrate = Button(master=inp_frame2, text="Migrate", highlightcolor='grey', width=20, command= lambda : migrate(self.inp_cluster.get(), self.out_cluster['UAT'].get(),self.out_cluster['HP'].get(),self.out_cluster['HP2'].get(), self.out_cluster['HP3'].get(), self.txt_scriptname.get()))

        lbl_scripter = Label(self.parent, text='Designed & Programmed by Nihal C', font=("Arial", 8))
        ###postioning
        lbl_scriptname.grid(row=0, column=0, sticky=E)
        self.txt_scriptname.grid(row=0, column=1, columnspan=4, sticky=W)
        
        lbl_inp_cluster.grid(row=1, column=0, sticky=E)
        rdio_uat_inp.grid(row=1, column=1, sticky=W)
        rdio_hp1_inp.grid(row=1, column=2, sticky=W)
        rdio_hp2_inp.grid(row=1, column=3, sticky=W)
        rdio_hp3_inp.grid(row=1, column=4, sticky=W)


        lbl_out_cluster.grid(row=2, column=0, sticky=E)
        cbox_uat_out.grid(row=2, column=1, sticky=W)
        cbox_hp1_out.grid(row=2, column=2, sticky=W)
        cbox_hp2_out.grid(row=2, column=3, sticky=W)
        cbox_hp3_out.grid(row=2, column=4, sticky=W)
        
        self.btn_migrate.grid(row=0,column=1)

        lbl_scripter.pack()


        ### Default option Selections



def migrate(*args):
    for i in args: print(i)



def main():
    root = Tk()
    app = myFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
