from django.shortcuts import render,redirect
from .forms import GeeksForm,HotelForm
import tensorflow as tf
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from django.http import HttpResponse

savedModel=load_model('base_model_0.h5')
def hotel_image_view(request):
    # classnames=['ABBOTTS BABBLER' 'ABBOTTS BOOBY']
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            X=form.save()
            im=X.Main_Img.path
            img = tf.io.read_file(im)
            img = tf.io.decode_image(img, channels=3)
            img = tf.image.resize(img, [224, 224])
            if True:
                 img= img/255.
            else:
                 img= img
            pred = savedModel.predict(tf.expand_dims(img, axis=0))
            print(pred)
            # if len(pred[0]) > 1:
            #     print(classnames[tf.argmax(pred[0])])
            # else:
            #     print(classnames[int(tf.round(pred[0]))])

            
    else:
        form = HotelForm()
    return render(request, 'home.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')