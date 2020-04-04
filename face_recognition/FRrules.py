from durable.lang import *
from FaceRecog import perform_recogintion



with ruleset('main'):
    @when_all(m.image == './images/dhoni.jpg')
    def jpgfind(c):
        perform_recogintion(c.m.image)

    #@when_all()
    #def  pngfind(c):
    #    perform_recogintion(c.m.image)
    #need to define many rules


post('main',{ 'image': './images/dhoni.jpg' })
