import mir3.modules.features as feat
import mir3.modules.tool.wav2spectrogram as spec
import mir3.modules.features.centroid as cent
import mir3.modules.features.rolloff as roll
import mir3.modules.features.flatness as flat
import mir3.modules.features.flux as flux
import mir3.modules.features.mfcc as mfcc
import mir3.modules.features.diff as diff
import mir3.modules.features.stats as stats
reload(stats)
import mir3.modules.features.join as join
import mir3.modules.tool.to_texture_window as tex

import constants

import numpy as np
import json
import sqlite3
import os

def mp3_to_wav(filename, directory):
    command = "mpg123 -w /tmp/tmp.wav " + directory + filename
    os.system(command)

def features_gtzan_mp3(filename, directory):
    mp3_to_wav(filename, directory)
    return features_gtzan("tmp.wav", "/tmp/")

def features_gtzan(filename, directory=""):
    # Calculate spectrogram (normalizes wavfile)
    converter = spec.Wav2Spectrogram()
    s = converter.convert(open(directory + filename), window_length=2048, dft_length=2048,
                window_step=1024, spectrum_type='magnitude', save_metadata=True)

    # Extract low-level features, derivatives, and run texture windows

    d = diff.Diff()
    features = (cent.Centroid(), roll.Rolloff(), flat.Flatness(), flux.Flux(), mfcc.Mfcc())

    all_feats = None
    for f in features:
        track = f.calc_track(s) # Feature track
        all_feats = join.Join().join([all_feats, track])
        dtrack = d.calc_track(track) # Differentiate
        all_feats = join.Join().join([all_feats, dtrack])
        ddtrack = d.calc_track(dtrack) # Differentiate again
        all_feats = join.Join().join([all_feats, ddtrack])

        # Texture window
        t = tex.ToTextureWindow().to_texture(all_feats, 40)

    # Statistics
    s = stats.Stats()
    d = s.stats([t], mean=True, variance=True)
    return d

def extract_all():
    query = "select id, title, artist, file from media where id not in " + \
            "(select media_id from features where algorithm='gtzan')"

    conn = sqlite3.connect(constants.dbfile)
    c = conn.cursor()
    #sweep = c.execute(query)
    #conn.commit()
    #conn.close()


    insertions = []
    for d in c.execute(query):
        #print filename
        print d[3]
        #conn = sqlite3.connect(constants.dbfile)

        filename = "../" + d[3]
        feats = features_gtzan_mp3(d[3], "../")

        json_data = json.dumps(feats.data.tolist())
        insertion_query = "insert into features (media_id, algorithm, value) " + \
                "values (" + str(d[0]) + ", 'gtzan', '" + str(json_data) + "');"

        insertions.append(insertion_query)
        print insertion_query

    for insertion_query in insertions:
        c.execute(insertion_query)
        conn.commit()

    conn.close()








