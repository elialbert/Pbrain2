import math, re, os, sys, string
import numpy

from pbrainlib.gtkutils import str2num_or_err, simple_msg, error_msg, \
     not_implemented, yes_or_no, FileManager, select_name, get_num_range, Dialog_FileSelection, Dialog_FileChooser, get_num_value

from data import EEGWeb, EEGFileSystem, EOI, Amp, Grids
from file_formats import FileFormat_BNI, W18Header, FileFormat_AxonAscii, FileFormat_NeuroscanAscii, FileFormat_AlphaomegaAscii, NeuroscanEpochFile



import pygtk
pygtk.require('2.0')
import gtk



class Pbrain2:

    self.extmap = { '.w18' : load_w18,
           '.bni' : load_bmsi,
           '.params' : load_params,
           '.epoch' : load_epoch,
           '.axonascii' : load_axonascii,
           '.neuroscanascii' : load_neuroscanascii,
           '.alphaomegaascii' : load_alphaomegaascii
           }



    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.
    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.win.connect("delete_event", self.delete_event)
        self.win.connect("destroy", self.destroy)
        self.win.set_border_width(10)

        self.button = gtk.Button("Hello World")
        self.button.connect("clicked", self.hello, None)
        self.win.add(self.button)
        self.button.show()
        self.win.show()
        
        self.fmanager = FileManager()

        dlg = Dialog_FileChooser(defaultDir=self.fmanager.get_lastdir(),
                                 okCallback=self.ok_callback,
                                 title='Select Neuroscanascii file',
                                 parent=self.win,
                                 previous_dirnames=self.fmanager.get_lastdirs())


    def ok_callback(self, dlg):
        fname = dlg.get_filename()
        
        fullpath =  dlg.get_filename()
        self.fmanager.set_lastdir(fullpath)
        dlg.destroy()
        
        if not os.path.exists(fullpath):
            error_msg(
                'Cannot find %s' % fullpath,
                title='Error',
                parent=self.win)
            
        basename, ext = os.path.splitext(fullpath)
        if not self.extmap.has_key(ext.lower()):
            error_msg(
                'Do not know how to handle extension %s in %s' % (ext, fullpath),
                title='Error',
                parent=self.win)
            
            return
        else:
            loader = self.extmap[ext.lower()]
            try: eeg = loader(fullpath)
            except ValueError, msg:
                msg = exception_to_str('Error loading EEG' )
                error_msg(msg, title='Error loading EEG',
                          parent=self.win)
                return
            else:
                if eeg is None: return 

        print "on_menuFileOpen_activate: eeg ext is ", ext
        if (eeg.get_file_type() != 1): # hack -- .bnis do not need .amp files
            amp = eeg.get_amp()
            if amp.message is not None:
                simple_msg(amp.message, title='Warning',
                           parent=self.win)
            
        #self.load_eeg(eeg)
        
        return False
        

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

        

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    pbrain2 = Pbrain2()
    pbrain2.main()
