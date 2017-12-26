from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class administrator(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, related_name = 'admin_profile')

    def create_user_profile(sender, instance, created, **kwargs):
        if created:#created == True if the User instance is save()'d.
            administrator.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)#when we save() a User model(since paramater 'sender = User')
    #post_save signal(django builtin signal) is activated which is connected to handler function 'create_user_profile', which is then executed.
    #Thus, when we create an instance of 'User' using 'User.objects.create_user()' internally save() is called and
    #hence it's UserProfile 'administrator' instance is created by the 'create_user_profile' function which is
    #initiated by post_save signal.....

    def __str__(self):
        return self.user.username

class participant(models.Model):
    creator = models.ForeignKey(administrator, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 50, blank = False)
    score = models.DecimalField(max_digits = 5, decimal_places = 2, help_text = 'Enter a score between 0.00 and 50.00')
    time_added = models.DateTimeField(auto_now_add = True, auto_now = False)
    time_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return str(self.full_name)
