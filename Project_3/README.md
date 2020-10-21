Project 3 -- SincNet 

Prerequisites: 
* Linux 
* Python 3.8
* GPU-capable Windows or macOS 
* NVIDIA driver

Installation
* TIMIT-corpus, available: https://www.kaggle.com/nltkdata/timitcorpus



* python TIMIT_preparation.py $TIMIT_FOLDER $OUTPUT_FOLDER data_lists/TIMIT_all.scp
<img width="464" alt="Screen Shot 2020-10-13 at 1 33 43 AM" src="https://user-images.githubusercontent.com/46795678/95819593-602c4680-0cf4-11eb-9203-2da2023cf372.png">
-- This deals with the TIMIT preparation, it removes the silences of the start-and-end of the TIMIT audios. Where $OUTPUT and $INPUT are replaced with the current TIMIT directory. 


Since there is something wrong with the SCC, which said my SCC quota has been full. And I'm using MacOS which does not contain a GPU. So I cannot continue with CUDA related training. I will go back once SCC gets back to work. 
