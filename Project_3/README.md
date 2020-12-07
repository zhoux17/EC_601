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

**UPDATE 

After deleting the unnecessary files in SCC, I moved files/ libraries to the group directory. (Storage Issue) 

Since there is no GPU in Macbook so I can only try on SCC. But I keep getting errors while update/ install the libraries.  (Not on the sudoers list)

I use virtual environemt and write the bash file for the GPU using in SCC, still not working. 

-----------------------------
**UPDATE

So i use another open-source library called mouth-open for this project, which also has used for the group project. 

***Usage***

python detect_videofile_mouth.py -f file_name.ext

*Requirements: 
scipy
imutils
numpy
dlib
cv2

--Basically this library uses the existing facial datasets to map 68 landamarks on the speaker's face. And do the calculation on the change of the length of the speaker's mouth. When the length exceed a certain threshold value the library will return that the speaker is opening his/ her mouth. This is how the library works to target who is the speaker over multiple speakers. 

--The multi-speaker identificaton can be either in real time or for a pre-recorded video file. 

If use the library in real time, use it as: 

python detect_open_mouth.py

and allow the access of webcam. 

Example: 
https://github.com/zhoux17/EC_601/blob/master/Project_3/mouth.png
