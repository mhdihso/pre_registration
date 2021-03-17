from django.db import models
from django.utils.translation import ugettext_lazy as _



class extra_qu(models.Model):
    TYPE_CHOISES = (
        ('1', 'Multiple options'),
        ('2', 'Descriptive '),
        ('3', 'File'),
        ('4', 'Data')
    )
    type_qu=models.TextField(max_length=1, choices=TYPE_CHOISES,default='2',null=False)
    text=models.CharField(max_length=200)

    def __str__(self):
        return self.text

class answer_qu(models.Model):
    qustion=models.ForeignKey(extra_qu,on_delete=models.CASCADE)
    answer_context=models.CharField(max_length=250)

class Create_preـregistration(models.Model):
    subject=models.CharField(max_length=250)
    price=models.PositiveIntegerField(default=None)
    school=models.CharField(max_length=150)
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class main(models.Model):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    mobile_phone = models.CharField(_('phone number'), max_length=11)
    national_id = models.CharField(_('national ID'), max_length=10)
    birth_date = models.DateField(_('data of birth'), blank=True, null=False)
    profile_pic = models.ImageField(_('profile picture'), upload_to='profile-pics')
    father_name=models.CharField(_('father name'),max_length=150)
    father_phone_number=models.CharField(_('father phone number'),max_length=11)

    def __str__(self):
        return self.first_name

class preـregistration(main):
        pre_id=models.ForeignKey(Create_preـregistration,on_delete=models.CASCADE,null=False,blank=False, related_name='pre_id')
        extra_qus=models.ManyToManyField(extra_qu,blank=True)


