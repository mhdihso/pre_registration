from django.db import models

class Create_preـregistration(models.Model):
    subject=models.CharField(max_length=250)
    price=models.PositiveIntegerField(default=None)
    school=models.CharField(max_length=150)
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class main(models.Model):
    pre=models.ForeignKey(Create_preـregistration,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile_phone = models.CharField(max_length=11, unique=True)
    home_number=models.CharField(max_length=10, unique=True)
    national_id = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(blank=False, null=False)
    profile_pic = models.ImageField(upload_to='profile-pics',blank=True, null=True)
    father_name=models.CharField(max_length=150)
    father_phone_number=models.CharField(max_length=11, unique=True)

class extra_qu(models.Model):
    TYPE_CHOISES = (
        ('1', 'Multiple options'),
        ('2', 'Descriptive '),
        ('3', 'File'),
        ('4', 'Data')
    )
    form_id=models.ForeignKey(Create_preـregistration,on_delete=models.CASCADE)
    type_qu=models.TextField(max_length=1, choices=TYPE_CHOISES,default='2',null=False)
    text=models.CharField(max_length=200)

    def __str__(self):
        return self.text

class extra_ans_multiple(models.Model):
    qus=models.ForeignKey(extra_qu,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=250)

    def __str__(self):
        return self.answer_text

class multiple_options(models.Model):
    option=models.CharField(max_length=150)
    Question=models.ForeignKey(extra_qu,on_delete=models.CASCADE)

class extra_ans_descriptive(models.Model):
    qus=models.ForeignKey(extra_qu,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=250)

    def __str__(self):
        return self.answer_text

class extra_ans_file(models.Model):
    qus=models.ForeignKey(extra_qu,on_delete=models.CASCADE)
    answer_text=models.FileField()

    def __str__(self):
        return self.answer_text

class extra_ans_date(models.Model):
    qus=models.ForeignKey(extra_qu,on_delete=models.CASCADE)
    answer_text=models.DateField()

    def __str__(self):
        return self.answer_text

