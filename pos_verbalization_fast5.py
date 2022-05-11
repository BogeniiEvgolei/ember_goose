# positions signals of Native dna
import h5py


def pos_virbalization_fast5(a, b, c):
    batches = 2
    print('total_batches =', batches)

    for j in range(batches):
        print('quackle_batch: {}, residue_batches: {}'.format(j+1, batches-1-j))

        with h5py.File('{}batch_{}.fast5'.format(a, j), 'r', rdcc_nbytes=1024**3) as file:
            for i in list(file.items()):

                readname = i[0]
                try:
                    trace = file['/{}/Analyses/RawGenomeCorrected_000/BaseCalled_template/Events'.format(readname)][:]

                except KeyError:
                    continue

                seq = ''.join([t[4].decode() for t in trace]).upper()                                                              
                seq_pos = b.find(seq)

                if seq_pos == -1:  continue

                for i in range(3, len(seq) - 4):
                    c[seq_pos+i].append(trace[i][0])

