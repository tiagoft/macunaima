
import librosa
import numpy as np


def features(filename):
    """Extracts features from a file. Returns a dictionary
    """
    y, sr = librosa.core.load(filename, mono=True)
    mfcc = librosa.feature.mfcc(y, sr, n_fft=2048, hop_length=512,
            power=1.0, n_mfcc=20)
    avg_mfcc = np.mean(mfcc, axis=1)
    dict_out = {'filename': filename, 'features': list(avg_mfcc)}

    return dict_out


if __name__ == "__main__":
    import sys
    import json
    fname = sys.argv[1]
    dout = features(fname)
    enc = json.JSONEncoder()
    print enc.encode(dout)
    exit()

