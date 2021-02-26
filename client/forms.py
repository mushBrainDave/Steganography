from io import BytesIO

from PIL import Image, PngImagePlugin, ImageFile
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Picture
from encoder import encoder


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'

    def clean_message(self):
        message = self.cleaned_data['message']
        #print(self.cleaned_data)
        cleaned_message = encoder.CreateMessage(message)
        return cleaned_message

    def clean_pic(self):
        cleaned = self.cleaned_data.copy()
        #print(self.cleaned_data)
        pic = cleaned.get('pic')
        #print(pic_open.read())
        #pic_rgb = pic_open.convert('RGB')
        #pic_rgb.save(BytesIO(), 'PNG', compression_level=100)
        #finished = encoder.Encode(pic_rgb, self.cleaned_data.get('message'))
        #pic.file = finished
        #print(pic.file.seek(63))
        #print(pic.file.read())
#        im = Image.open(pic)
        im = pic.file
        a = pic.chunks()
        print(next(a))
        #tig = PngImagePlugin.PngStream(im)
        #ting = PngImagePlugin.getchunks(im)
        #print(ImageFile.Parser.feed(im))
        #print(type(im))
        #print(type(pic.file.read()))

#        im.convert('RGB')
#        r = BytesIO()
#        print(type(im))
#        im.save(r, 'PNG', compress_level=0)
#        print(type(im))
#        print(im.load())
        finished = encoder.Encode(im, self.cleaned_data.get('message'))
        pic.file = finished
        return pic



        #print(self.cleaned_data['pic'].__repr__())
        #pic = self.cleaned_data['pic']

        #pic2 = pic.file
        #print(self.cleaned_data['pic'].__repr__())

        #print(type(pic2))
        #cleaned_pic = encoder.Encode(pic2, self.cleaned_data['message'])
        #pic.file = cleaned_pic
        #print(self.cleaned_data['pic'].open().read())

        #attribute = [a for a in dir(self.cleaned_data['pic']) if not a .startswith("__")]
        #field_name = self.cleaned_data['pic'].field_name
        #name = self.cleaned_data['pic'].name
        #content_type = self.cleaned_data['pic'].content_type
        #size = self.cleaned_data['pic'].size
        #charset = self.cleaned_data['pic'].charset
        #new_file = InMemoryUploadedFile(pic2, field_name, name, content_type, size, charset)
        #print(new_file.__repr__())
        #print(new_file['pic'].open().read())
        #print(self.cleaned_data['pic'].field_name)

        #print(type(cleaned_pic))
        #print(type(pic))
        #print(pic.size)
        #print(pic.file)

#        return pic
