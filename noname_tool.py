#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: 07.05.2021
#@author: SWW 2021 team
#@contact: support@noname_tool.com

import argparse


def count_GGG_triplets(sequence):
    '''Count GGG triplets in given sequence.
    
    Parameters:
    sequence (string): DNA sequence

    Returns:
    int: A number of GGG triplets
    '''
    return sequence.count('GGG')

def fasta_reader(fasta_file):
    """
    Args:
        fasta_file: path to genome in fasta format

    Returns:
         dictionary with key == fasta header, value == sequence
    """
    pass


def genome_N50(fasta_dictionary):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)

    Returns:
        N50 characteristics of genome
    """
    pass


def genome_length(fasta_dictionary):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)

    Returns:
        genome_length
    """
    pass


def genome_gc(fasta_dictionary):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)

    Returns:
        genome gc content (%)
    """
    pass


def nucleotide_frequency(fasta_dictionary):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)

    Returns:
        dictionary with frequency of each nucleotide, key == k-mer (sequence), value == frequency
    """
    pass


def kmer_frequency(fasta_dictionary, k):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)
        k: length of k-mer sequence

    Returns:
        dictionary with k-mer frequency, key == k-mer (sequence), value == frequency
    """
    pass


def orf_finder(fasta_dictionary):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)

    Returns:
        dictionary with key == number of ORF, value == array with positions of start and stop codon
    """
    pass


def codon_frequency(fasta_dictionary):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)

    Returns:
        dictionary with key == codon (e.g. "ATG"), value == frequency of codone
    """
    pass


def aminoacid_frequency(fasta_dictionary):
    """
    Args:
        fasta_dictionary: dictionary with key == fasta header, value == sequence (fasta_reader function)

    Returns:
        dictionary with key == aminoacid (e.g. "M"), value == frequency of aminoacid
    """
    pass


def main(input_file, output_file):
  
    with open(input_file) as fh:
        pass
    
    for sequence in sequences:
      results = {}
      results['ggg_counts'] = count_GGG_triplets(sequence)
    
    with open(output_file, 'w') as fw:
        pass

import os
import csv 
def write_in_file(parser, cmers, ORF1, ORF2, codons, amino):  
    parser = {}
    GC_amount = {}
    n50 = {}
    cmers = {}
    ORF1 = {}
    ORF2 = {}
    codons = {}
    amino = {}

    dicts = parser, GC_amount, n50, cmers, ORF1, ORF2, codons, amino
    
    with open('wril.csv', 'w') as file:
        writer = csv.writer(ofile, delimiter='\t')
        for key in parser.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        for key in GC_amount.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        for key in n50.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        for key in cmers.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        for key in ORF1.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        for key in ORF2.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        for key in codons.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        for key in amino.iterkeys():
            writer.writerow([key] + [d[key] for d in dicts])
        writer.writerow(['parser', 'GC_amount', 'n50', 'cmers', 'ORF1', 'ORF2', 'codons', 'amino'])
        file.close() 
         
         

            
  

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Super noname tool!')
    parser.add_argument('-i','--input', help='Input file', required=True)
    parser.add_argument('-o','--output', help='Output file', required=True)
    args = vars(parser.parse_args())
    
    main(input_file, output_file)
