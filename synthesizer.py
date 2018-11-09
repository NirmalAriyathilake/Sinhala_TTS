# -*- coding: utf-8 -*-
# /usr/bin/python2

from __future__ import print_function

import os

from hyperparams import Hyperparams as hp
import numpy as np

import wave
from pydub import AudioSegment


def synthesize(inputtext):
    print("Started")
    # inputtext = 'piligannawa'
    # inputtext = 'ticket wen kireeme sewawa wetha saadharayen piligannawa'
    # Load data
    print("Loading data")
    fname = os.path.join(hp.data, 'transcript5.csv')
    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    print("Data loaded")

    # Load graph
    graph = {}

    for line in content:
        line = line.split("|")
        graph[line[1]] = line[0] + ".wav"

    print("Graph loaded")
    # Feed forward
    inputline = inputtext.split(" ")
    infiles = []

    for word in inputline:
        # if graph.has_key(word):
        path = os.path.join(hp.data + '/wavs', graph[word])
        infiles.append(path)

    # Generate wav files
    print("Synthesizing...")

    if not os.path.exists(hp.sampledir): os.makedirs(hp.sampledir)
    outfile = os.path.join(hp.sampledir, 'test.wav')

    # data = []
    # for infile in infiles:
    #     w = wave.open(infile, 'rb')
    #     data.append([w.getparams(), w.readframes(w.getnframes())])
    #     w.close()
    #
    # output = wave.open(outfile, 'wb')
    # output.setparams(data[0][0])
    #
    # for i in range(len(data)):
    #     output.writeframes(data[i][1])
    #
    # output.close()

    comb = AudioSegment.empty()
    for infile in infiles:
        s = AudioSegment.from_wav(infile)
        comb += s

    comb.export(outfile, format="wav")


if __name__ == '__main__':
    synthesize()
    print("Done")
