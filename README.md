# ComputerVision-DeepLearning
Various computer vision problems solved using concepts of deep learning

- clone this repository
- run "jupyter notebook" at root folder

1. Cricket Shot classification into off-side and on-side shots
    - Dataset created using google_images_download python library. Search results were not good so dataset required manual cleaning.
    - "cover drive cut cricket shot", and "defense shot cricket" were used as argument to image_download script for label:"0"
    - "Sweep shot cricket", "pull hook shot cricket" were used as arguments to iamge_download script for label:"1"
    - Pre-trained VGG-16 model used as feature extractor
    - Small ConvNet followed by Dense layers trained to decide shot class
    - Keras used to build model
2. Lung Segmentation from CT images
    - Dataset downloaded from https://www.kaggle.com/c/data-science-bowl-2017/data
    - Various U-Net architectures experimented with to understand accuracy vs efficiency tradeoff
    - Trained networks with dice coefficient as loss
    - Some results shown in ipynb
3. Pneumonia detection from chest X-rays
    - Dataset downloaded from https://www.kaggle.com/parthachakraborty/pneumonia-chest-x-ray
    - Built and trained Convolutional Neural Networks of various size.
    - CLassification was between normal and pneumonia cases. Binary cross-entropy loss was used.
    - Accuracy, precision and recall of the models was examined and confusion matrix plotted
4. Scenery Detection
    - Dataset created with google_images_download python library.
    - Classes are 0: city; 1: ocean; 2: canyon; 3: desert; 4: mountain; 5: river; 6: waterfall
    - Convolutional neural network trained from scratch on 1728 training examples. Results were not very good.
    - Used Convolutional layers of VGG-16 as a feature extractor. This transfer learning strategy achieves better accuracy.
    - Some wrong predictions are shown to understand possible reasons for error
