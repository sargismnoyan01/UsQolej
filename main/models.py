from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class AboutCollege(models.Model):
    txt=models.TextField('Գլխավոր էջ՝ քոլեջի մասին')
    address=models.CharField('Հասցե',max_length=100)


    def __str__(self) -> str:
        return self.address
    
    class Meta:
        verbose_name='Գլխավոր էջի տվյալներ'
        verbose_name_plural='Գլխավոր էջի տվյալներ'

class Professions(models.Model):
    name=models.CharField('Մասնագիտության անվանում',max_length=100)
    img=models.ImageField('Նկար',upload_to='Professions imagers')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Մասնագիտություններ'
        verbose_name_plural='Մասնագիտություններ'

class ProfDetail(models.Model):
    name=models.ForeignKey(Professions,on_delete=models.CASCADE,related_name='profdetail')
    info=models.TextField('Բաժնի մասին տեղեկություններ')

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name='մանրամասն տեղեկություններ'
        verbose_name_plural='մանրամասն տեղեկություններ'   

class Staffs(models.Model):
    name=models.CharField('Անուն ազգանուն',max_length=50)
    prof=models.CharField('Զբաղեցրած պաշտոն',max_length=50)
    img=models.ImageField('Նկար',upload_to='Staffs')


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Աշխատակազմ'
        verbose_name_plural='Աշխատակազմ'    



class Questions(models.Model):
    question=models.CharField('Հարցը',max_length=255)
    answer=models.TextField('Պատասխան')

    def __str__(self) -> str:
        return self.question
    
    class Meta:
        verbose_name='Հարց և պատասխան'
        verbose_name_plural='Հարց և պատասխան'


class ContactUs(models.Model):
    address=models.CharField('Հասցե',max_length=100)
    phone=PhoneNumberField('Հեռախոսահամար +374-ով սկսվող')
    email=models.EmailField('Email')
    facebook=models.URLField('Facebook',blank=True)
    linkedin=models.URLField('LinkedIn',blank=True)
    instagram=models.URLField('Instagram',blank=True)


    def __str__(self) -> str:
        return self.address
    
    class Meta:
        verbose_name='Կոնտակտային տվյալներ'
        verbose_name_plural='Կոնտակտային տվյալներ'
        
class Dimord(models.Model):
    title=models.CharField('Վերնագիր',max_length=255)
    subtitle=models.CharField('Տարբերվող տողը՝ տեքստի սկզբում ',max_length=500)
    text=models.TextField('Տեքստի մնացած հատված')
    img=models.ImageField('Նկար',upload_to='dimord',null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='Դիմորդ'
        verbose_name_plural='Դիմորդ'

class PDFiles(models.Model):
    name=models.CharField('Անունը',max_length=155)
    file=models.FileField('pdf Ֆայլը',upload_to='pdf')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='PDF ֆայլեր'
        verbose_name_plural='PDF ֆայլեր'

class MyVideo(models.Model):
    video=models.FileField('Տեսանյութ',upload_to='video')

    def __str__(self) -> str:
        return f'{self.video}'
    
    class Meta:
        verbose_name='Տեսանյութ'
        verbose_name_plural='Տեսանյութ'


class Contact(models.Model):
    name=models.CharField('Անուն',max_length=50)
    subject=models.CharField('Ենթատեքստ',max_length=50)
    message=models.TextField('Հաղորդագրություն')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Հաղորդագրություններ'
        verbose_name_plural='Հաղորդագրություններ'

class SubStuffs(models.Model):
    nam=models.ForeignKey(Staffs,on_delete=models.CASCADE,related_name='namee')
    message=models.TextField('Մեկնաբանություն')

    def __str__(self) -> str:
        return f'{self.nam}'
    
    class Meta:
        verbose_name='Աշխատակազմի կարծիքներ'
        verbose_name_plural='Աշխատակազմի կարծիքներ'