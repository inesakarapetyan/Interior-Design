from django.db import models

# Create your models here.
class Logo(models.Model):
    img = models.ImageField('Logo image', upload_to='logo')

    def __str__(self):
        return 'Logo'

class HomeInfo(models.Model):
    static_text = models.CharField("HomeInfo", max_length=50)
    dinamic_text1 = models.CharField("HomeInfo text 1", max_length=50)
    dinamic_text2 = models.CharField("HomeInfo text 2", max_length=50)
    dinamic_text3 = models.CharField("HomeInfo text 3", max_length=50)
    about = models.TextField("HomeInfo")
    button_name = models.CharField("HomeInfo", max_length=50)

    def __str__(self):
        return f'{self.ststic_text}'


class Intro(models.Model):
    intro = models.CharField('IntroPage', max_length=50)
    main_text = models.TextField("IntroPage")
    other_text = models.TextField("IntroPage")
    img = models.ImageField("IntroPage", upload_to='intro', blank=True)

    def __str__(self):
        return f'{self.intro}'
    

class Explain(models.Model):
    text1 = models.CharField("Explain", max_length=50)
    text2 = models.TextField("Explain")
    text3 = models.CharField("Explain", max_length=50)
    text4 = models.TextField("Explain")
    text5 = models.CharField("Explain", max_length=50)
    text6 = models.TextField("Explain")

    def __str__(self):
        return f'{self.text1}'

class Project(models.Model):
    image = models.ImageField("Project", upload_to='project')
    name1 = models.CharField('Project name', max_length=50)
    name2 = models.CharField('Project name2', max_length=50)
    text1 = models.TextField('Project text1')
    text2 = models.TextField('Project text1')
      
      
    def  __str__(self):
          return self.name1

class Picture(models.Model):
    # img1 = models.ImageField("Image", upload_to='picture')
    # img2 = models.ImageField("Image", upload_to='picture')
    # img3 = models.ImageField("Image", upload_to='picture')
    # img4 = models.ImageField("Image", upload_to='picture')
    # img5 = models.ImageField("Image", upload_to='picture')
    # img6 = models.ImageField("Image", upload_to='picture')
    # img7 = models.ImageField("Image", upload_to='picture')
    # img8 = models.ImageField("Image", upload_to='picture')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proj', blank=True)
    name = models.CharField('Picture', max_length=50)
    img = models.ImageField('Image', upload_to='picture', blank=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    desc = models.TextField('Description')
    address = models.TextField('Address')
    phone1 = models.CharField('Phone1',max_length=50)
    phone2 = models.CharField('Phone2', max_length=50)
    mail = models.EmailField('Email')
    fb = models.TextField('Facebook')
    insta = models.TextField('Instagram')

    def __str__(self):
        return 'ContactInfo'
    


class ContactUs(models.Model):
    name = models.CharField('Name', max_length=50)
    mail = models.EmailField('Email')
    message = models.TextField('Your message')

    def __str__(self):
        return self.name