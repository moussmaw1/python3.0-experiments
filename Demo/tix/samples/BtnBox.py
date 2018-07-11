# -*-mode: python; fill-column: 75; tab-width: 8; coding: iso-latin-1-unix -*-
#
# $Id: BtnBox.py 68310 2009-01-04 19:01:19Z benjamin.peterson $
#
# Tix Demostration Program
#
# This sample program is structured in such a way so that it can be
# executed from the Tix demo program "tixwidgets.py": it must have a
# procedure called "RunSample". It should also have the "if" statment
# at the end of this file so that it can be run as a standalone
# program.

# This file demonstrates the use of the tixButtonBox widget, which is a
# group of TK buttons. You can use it to manage the buttons in a dialog box,
# for example.
#

import tkinter.tix

def RunSample(w):
    # Create the label on the top of the dialog box
    #
    top = tkinter.tix.Label(w, padx=20, pady=10, bd=1, relief=tkinter.tix.RAISED,
                    anchor=tkinter.tix.CENTER, text='This dialog box is\n a demonstration of the\n tixButtonBox widget')

    # Create the button box and add a few buttons in it. Set the
    # -width of all the buttons to the same value so that they
    # appear in the same size.
    #
    # Note that the -text, -underline, -command and -width options are all
    # standard options of the button widgets.
    #
    box = tkinter.tix.ButtonBox(w, orientation=tkinter.tix.HORIZONTAL)
    box.add('ok', text='OK', underline=0, width=5,
            command=lambda w=w: w.destroy())
    box.add('close', text='Cancel', underline=0, width=5,
            command=lambda w=w: w.destroy())
    box.pack(side=tkinter.tix.BOTTOM, fill=tkinter.tix.X)
    top.pack(side=tkinter.tix.TOP, fill=tkinter.tix.BOTH, expand=1)

if __name__ == '__main__':
    root = tkinter.tix.Tk()
    RunSample(root)
    root.mainloop()
