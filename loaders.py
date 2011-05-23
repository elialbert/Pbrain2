Class Loaders:



    def load_w18(fullpath):
    assert(os.path.exists(fullpath))
    basename, filename = os.path.split(fullpath)
    fh = file(fullpath, 'rb')
         
    header = W18Header(fh)
    params = {
        'filename'        : filename,
        'date'            : header.currtime,
        'description'     : '',
        'channels'        : 18,
        'freq'            : 200,
        'classification'  : 99,
        'file_type'       : W18,
        'behavior_state'  : 99,
        }

    eeg = EEGFileSystem(fullpath, params)
    return eeg

def load_bmsi(bnipath):

    bni = FileFormat_BNI(bnipath)
    basename, ext = os.path.splitext(bnipath)
    
    if os.path.exists(basename):    
        fullpath = basename
    elif os.path.exists(basename + '.eeg'):
        fullpath = basename + '.eeg'
    else:
        fullpath = fmanager.get_filename(
            title='Select EEG File accompanying this BNI file')

    eeg = bni.get_eeg(fullpath)
    return eeg


def load_epoch(fname):
    epoch = NeuroscanEpochFile(fname)
    return epoch.eeg

def load_params(path):
    params = {}
    for line in file(path):
        line = line.strip()
        if not len(line): continue
        if line.startswith('#'): continue

        k,v = line.split(':',1)
        k = k.strip()
        v = v.strip()
        if k in ('channels', 'pid', 'freq', 'classification', 'file_type', 'behavior_state') :
            v = int(v)
        params[k] = v

    eegfile = params['eegfile']
    if not os.path.exists(eegfile):
        error_msg('Cannot find eeg file "%s"'%eegfile)
        return

    eeg = EEGFileSystem(eegfile, params)
    return eeg


def load_axonascii(path):
    axonascii = FileFormat_AxonAscii(path)
    return axonascii.eeg

def load_alphaomegaascii(path):
    alphaomegascii = FileFormat_AlphaomegaAscii(path)
    return alphaomegascii.eeg

def load_neuroscanascii(path):
    try:
        neuroscanascii = FileFormat_NeuroscanAscii(path)
    except IOError, msg:
        print "load_neuroscanascii(): msg=", msg
        error_msg(msg, title='Error', parent=parent)
                    
    return neuroscanascii.eeg



    def load_w18(fullpath):
    assert(os.path.exists(fullpath))
    basename, filename = os.path.split(fullpath)
    fh = file(fullpath, 'rb')
         
    header = W18Header(fh)
    params = {
        'filename'        : filename,
        'date'            : header.currtime,
        'description'     : '',
        'channels'        : 18,
        'freq'            : 200,
        'classification'  : 99,
        'file_type'       : W18,
        'behavior_state'  : 99,
        }

    eeg = EEGFileSystem(fullpath, params)
    return eeg

def load_bmsi(bnipath):

    bni = FileFormat_BNI(bnipath)
    basename, ext = os.path.splitext(bnipath)
    
    if os.path.exists(basename):    
        fullpath = basename
    elif os.path.exists(basename + '.eeg'):
        fullpath = basename + '.eeg'
    else:
        fullpath = fmanager.get_filename(
            title='Select EEG File accompanying this BNI file')

    eeg = bni.get_eeg(fullpath)
    return eeg


def load_epoch(fname):
    epoch = NeuroscanEpochFile(fname)
    return epoch.eeg

def load_params(path):
    params = {}
    for line in file(path):
        line = line.strip()
        if not len(line): continue
        if line.startswith('#'): continue

        k,v = line.split(':',1)
        k = k.strip()
        v = v.strip()
        if k in ('channels', 'pid', 'freq', 'classification', 'file_type', 'behavior_state') :
            v = int(v)
        params[k] = v

    eegfile = params['eegfile']
    if not os.path.exists(eegfile):
        error_msg('Cannot find eeg file "%s"'%eegfile)
        return

    eeg = EEGFileSystem(eegfile, params)
    return eeg


def load_axonascii(path):
    axonascii = FileFormat_AxonAscii(path)
    return axonascii.eeg

def load_alphaomegaascii(path):
    alphaomegascii = FileFormat_AlphaomegaAscii(path)
    return alphaomegascii.eeg

def load_neuroscanascii(path):
    try:
        neuroscanascii = FileFormat_NeuroscanAscii(path)
    except IOError, msg:
        print "load_neuroscanascii(): msg=", msg
        error_msg(msg, title='Error', parent=parent)
                    
    return neuroscanascii.eeg




    self.extmap = { '.w18' : load_w18,
           '.bni' : load_bmsi,
           '.params' : load_params,
           '.epoch' : load_epoch,
           '.axonascii' : load_axonascii,
           '.neuroscanascii' : load_neuroscanascii,
           '.alphaomegaascii' : load_alphaomegaascii
           }



    self.extmap = { '.w18' : load_w18,
           '.bni' : load_bmsi,
           '.params' : load_params,
           '.epoch' : load_epoch,
           '.axonascii' : load_axonascii,
           '.neuroscanascii' : load_neuroscanascii,
           '.alphaomegaascii' : load_alphaomegaascii
           }

