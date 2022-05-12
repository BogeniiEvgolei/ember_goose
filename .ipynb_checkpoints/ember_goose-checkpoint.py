from argparse import ArgumentParser
from collections import defaultdict
from Bio.SeqIO import parse
from pos_verbalization_fast5 import pos_virbalization_fast5
from cheker import duck_filter
import copy
import os
from lib_ember_goose import LIB_ember_goose

parser = ArgumentParser()

parser.add_argument('--fast5_basedirs', type=str, required=True)
parser.add_argument('--reference_genome', type=str, required=True)
parser.add_argument('--loon_nest', type=str, help='path to quackles files',  required=True)

args = parser.parse_args()


folder_bathes = args.fast5_basedirs
ref_genome = args.reference_genome

LIB_native_dna_pos_signals = defaultdict(list)


ref_file = parse(ref_genome, format='fasta') 
for rec in ref_file:
    reference = str(rec.seq)
    break

    
print('{}{}{}'.format('\n', '--- positions verbalization your fast5 ---', '\n'))


pos_virbalization_fast5(folder_bathes, reference, LIB_native_dna_pos_signals)


base_distinction = {pos:[[], [], []] for pos in LIB_native_dna_pos_signals} # - для каждой позиции создаем три списка: мотив, p-lue, effect_size
special_destinction = copy.deepcopy(base_distinction)



print('{}{}{}'.format('\n', '--- duck filter on the spot ---', '\n'))


duck_filter(LIB_native_dna_pos_signals, LIB_ember_goose, reference, base_distinction, special_destinction)

os.chdir(args.loon_nest)
os.mkdir('Ember_goose')


sorted_pos = list(base_distinction.keys())
sorted_pos.sort()


with open ('Ember_goose/pos_genome_distinction.txt', 'w') as penman:
    
    for pos in sorted_pos:   
        penman.write('{}{} {} {} {} {}'.format(pos, ':\t', base_distinction[pos][1],  base_distinction[pos][2],  base_distinction[pos][0], '\n'))
        

        
        
spec_sort_dist = list(special_destinction.keys())
spec_sort_dist.sort()


with open ('Ember_goose/pos_genome_special_distinction.txt', 'w') as penman:
    
    for pos in spec_sort_dist:   
        penman.write('{}{} {} {} {} {}'.format(pos, ':\t', special_destinction[pos][1],  special_destinction[pos][2],  special_destinction[pos][0], '\n'))
        
        
print('{}{}'.format('\n', '--- duck fucked up'))
print('{}{}'.format('\n', '--- good day:)'))