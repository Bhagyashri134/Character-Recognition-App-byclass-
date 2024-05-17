# Character Recognition App(byclass)

EMNIST(Extended-MNIST) dataset is a set of handwritten character digits derived from the NIST Special Database 19  and converted to a 28x28 pixel image format.
https://www.kaggle.com/datasets/crawford/emnist

Dataset Summary

There are six different splits provided in this dataset. A short summary of the dataset is provided below:

[EMNIST ByClass](https://github.com/Pooja12312/Character-Recognition-App-byclass-/blob/main/Emnist_byclass_Model.ipynb): 814,255 characters. 62 unbalanced classes.<br>
EMNIST ByMerge: 814,255 characters. 47 unbalanced classes.<br>
EMNIST Balanced: 131,600 characters. 47 balanced classes.<br>
EMNIST Letters: 145,600 characters. 26 balanced classes.<br>
EMNIST Digits: 280,000 characters. 10 balanced classes.<br>
EMNIST MNIST: 70,000 characters. 10 balanced classes.<br>

## Our aim is to get 
![output(2)](https://github.com/Pooja12312/Character-Recognition-App-byclass-/blob/main/Interface/output%20(2).png)

- **Emnist_byclass_Model.ipynb** consists dataset download from kaggle, visualization, preprocessing on dataset and creat a model  

- **app.py** consists of "model - 32x64 bs_1024 ep_5 acc_0.871 loss_0.345  (1).h5" model which is added in the repository, by visiting the Kaggle Notebook URL, one can try out the code and download the model with their required specifications, so as to avoid version errors while deploying over web.
## Output of app.py

### Interface 1
![output(2)](https://github.com/Pooja12312/Character-Recognition-App-byclass-/blob/main/Interface/st1.png)

### Interface 2

![output(2)](https://github.com/Pooja12312/Character-Recognition-App-byclass-/blob/main/Interface/str2.png)

In summary, this code creates a streamlit based handwritten charactor recognition application where users can upload an image containing handwritten charactor. The application then uses the Downloaded Model to recognize and display the text from these inputs through a user-friendly interface it also transfer the style of input charector in the give font file (calligraphy). 
