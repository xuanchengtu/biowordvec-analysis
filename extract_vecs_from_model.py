import gensim
from gensim.models import KeyedVectors as KV
import pandas as pd
import csv
import json

VECS_DB = 'PubMed-and-PMC-w2v.bin' # <--- The model file 

def main():
    # Load the model
    print('Loading model...')
    model = KV.load_word2vec_format(VECS_DB, binary=True)
    print('end')
    
    # Create dictionary 
    with open("PanglaoDB_markers_27_Mar_2020.tsv") as file:
        reader = csv.reader(file, delimiter="\t")
        tsvData = list(reader)
        header = tsvData[0]
        data = tsvData[1:]
        
    species = header.index("species")
    ogs = header.index("official gene symbol")
    ct = header.index("cell type")
    
    ct_to_genes = {}
    for i in data:
        if not "Hs" in i[species]:
            continue
        if not i[ct] in ct_to_genes:
            ct_to_genes[i[ct]] = []
        ct_to_genes[i[ct]].append(i[ogs])
    
    # Save the JSON file storing which word pairs with which word
    with open("wordpairs.json", 'w', encoding="utf-8") as f:
        json.dump(ct_to_genes, f, indent=2)

    # Initialize a set for all the words. First storing
    # all of the cell types
    our_words = set(ct_to_genes.keys())

    # Add all genes to the set of words
    for genes in ct_to_genes.values():
        our_words.update(genes)

    # Get all words in the model
    # modal.vocab is deprecated. Updated to the newest feature of gensim. original: model_words = set(model.vocab.keys())
    model_words = set(list(model.index_to_key))
    
    # See which words are in the model using set intersection
    our_words_in_model = our_words & model_words

    # Sort the words so we have set order
    our_words_in_model = sorted(our_words_in_model)

    # Get the vectors for all these words
    word_vectors = model[our_words_in_model]

    # Output the vectors to a file
    df_vecs = pd.DataFrame(
        data=word_vectors,
        index=our_words_in_model
    )

    # Write file
    df_vecs.to_csv('cell_type_genes_word_vecs.tsv', sep='\t')

    # Create a table for our cell type gene pairs where the
    # first column is a cell type and the second is a gene
    ct_gene_pairs = []
    for ct, genes in ct_to_genes.items():
        for gene in genes:
            ct_gene_pairs.append((ct, gene))

    # Create dataframe for cell type-gene pairs
    df_pairs = pd.DataFrame(
        data=ct_gene_pairs,
        columns=['cell_type', 'gene']
    )      

    # Write file
    df_pairs.to_csv('cell_type_gene_pairs.tsv', sep='\t')


if __name__ == '__main__':
    main()
