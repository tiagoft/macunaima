
import librosa
import numpy as np

vnorm = np.array([114.7830736292783, -82.39487127664428, 24.925682421505325,
    -32.13117249367375, -11.134384464789452, -8.976907403216034,
    -13.01583047782167, -9.534425036589369, -0.4247558721367258,
    -4.5444638281851875, -5.321650853024308, -8.222924785877762,
    -5.770050128647196, -10.454824210451994, -1.9041227602110489,
    -2.1543844227708697, -1.6057728302115553, -2.273383303349304,
    3.241308565193654])

def features(filename):
    """Extracts features from a file. Returns a dictionary
    """
    y, sr = librosa.core.load(filename, mono=True)
    y -= np.mean(y)
    y /= (np.var(y)**0.5)
    mfcc = librosa.feature.mfcc(y, sr, n_fft=2048, hop_length=512,
            power=1.0, n_mfcc=20)
    avg_mfcc = np.mean(mfcc, axis=1)[1:]
    avg_mfcc /= vnorm
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

