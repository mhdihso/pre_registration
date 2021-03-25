from django.db import models

class PreRegistration(models.Model):
    subject=models.CharField(max_length=250)
    price=models.PositiveIntegerField(default=None)
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        st=self.id
        stri=str(st)
        return stri
class MainForm(models.Model):
    pre=models.ForeignKey(PreRegistration,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile_phone = models.CharField(max_length=11, unique=True)
    home_number=models.CharField(max_length=10, unique=True)
    national_id = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(blank=False, null=False)
    profile_pic = models.ImageField(upload_to='profile-pics',blank=True, null=True)
    father_name=models.CharField(max_length=150)
    father_phone_number=models.CharField(max_length=11, unique=True)

class ExtraQu(models.Model):
    TYPE_CHOISES = (
        ('1', 'Multiple options'),
        ('2', 'Descriptive '),
        ('3', 'Date')
    )
    form_id=models.ForeignKey(PreRegistration,on_delete=models.CASCADE)
    type_qu=models.TextField(max_length=1, choices=TYPE_CHOISES,default='2',null=False)
    text=models.CharField(max_length=200)

class MultipleOptions(models.Model):
    Question=models.ForeignKey(ExtraQu,on_delete=models.CASCADE)

class MultipleOptionsData(models.Model):
    multiple_add=models.ForeignKey(MultipleOptions,on_delete=models.CASCADE,related_name='options')
    option=models.CharField(max_length=150)

class ExtraAns(models.Model):
    form_id=models.ForeignKey(MainForm,on_delete=models.CASCADE)
class ExtraAnsData(models.Model):
    extra_answers=models.ForeignKey(ExtraAns,on_delete=models.CASCADE,related_name='answers')
    answer_text=models.CharField(max_length=250)
    qus=models.ForeignKey(ExtraQu,on_delete=models.CASCADE)
