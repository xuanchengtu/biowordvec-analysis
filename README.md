# WordVector Visualization
Goals of this project:
1. Gather word pairs and associated word vectors to be used for downstream methods development and validation. Word vectors are extracted from BioWordVec model and loaded using Gensim: https://www.nature.com/articles/s41597-019-0055-0. Each word pair pairs a cell type word and a marker gene word that relates to each other based on the data from PanglaoDB: https://panglaodb.se
2. For marker gene words, different variations of the same word can be found in the model. Variations include single/plural forms, all letters in upper/lower case, initial letter in upper/lower case, etc. We want to know if variations of the same word have similar word vectors or not. Firstly, we reduce the original 200-dimentions word vectors to 2-dimentions using PCA and TSNE with different settings. Then, we plot those 2-D points using matplotlib scatter plots. We want to see whether points of words that are variations of the same words appear to cluster together or not.

### Folder description
img: contains scatter plot images that shows dimentionality-reduced word vector data
output_data: contains data of cell-gene word pairs, word variations that are found in the model, word vectors, and dimentionality-reduced word vectors in json and tsv format.
raw_data: contains data from PanglaoDB that includes cell types and marker genes that are related. The BioWordVec model data is not uploaded to GitHub since its file size is too big.
