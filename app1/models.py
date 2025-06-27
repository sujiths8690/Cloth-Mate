from django.db import models
<<<<<<< HEAD
from django.db.models import BigAutoField


# Create your models here.
class BankAd(models.Model):
    ad_id=models.AutoField(primary_key=True)
    ad_img=models.ImageField(upload_to='bankad/',null=True)

    class Meta:
        db_table='bankad_table'


class AccountType(models.Model):
    acc_type = models.AutoField(primary_key=True)
    acc_name = models.CharField(max_length=100)
    min_balance=models.IntegerField()

    def __str__(self):
        return f"{self.acc_name}:{self.min_balance}"

    class Meta:
        db_table = 'acc_table'

class UserClass(models.Model):
    user_id=models.BigAutoField(primary_key=True)
    user_first_name=models.CharField(max_length=100)
    user_last_name=models.CharField(max_length=100)
    user_sex=models.CharField(max_length=10)
    user_dob=models.DateField()
    user_age=models.IntegerField()
    user_email=models.EmailField()
    user_mobile=models.BigIntegerField()
    user_address=models.CharField(max_length=100)
    user_city=models.CharField(max_length=20)
    user_state=models.CharField(max_length=20)
    user_pincode=models.IntegerField()
    user_password=models.CharField(max_length=20)
    user_balance=models.IntegerField(default=0)
    acc_type=models.ForeignKey(AccountType,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id}:{self.user_first_name} {self.user_last_name}"

    class Meta:
        db_table='user_table'

class Transaction(models.Model):
    transaction_id=models.BigAutoField(primary_key=True)
    transaction_method=models.CharField(max_length=10)
    transaction_amount=models.IntegerField()
    transaction_details = models.CharField(max_length=300)
    user=models.ForeignKey(UserClass,on_delete=models.CASCADE)

    class Meta:
        db_table='transaction_table'
=======

# Create your models here.

class Gender(models.Model):
    gender_id=models.CharField(max_length=100)
    gender_name=models.CharField(max_length=100)
    gender_carousal_img=models.ImageField(upload_to="genderimg/",null=True)
    gender_card_img=models.ImageField(upload_to="genderimg/",null=True,blank=True)

    def __str__(self):
        return f"{self.gender_id}: {self.gender_name}"


    class Meta:
        db_table='gender'

class ClothType(models.Model):
    cloth_id=models.AutoField(primary_key=True)
    cloth_type=models.CharField(max_length=100)
    cloth_type_img=models.ImageField(upload_to="clothtypeimg/",null=True)
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cloth_type}: {self.gender.gender_name}"


    class Meta:
        db_table='cloth_type'

class TypeCat(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=200,null=True)
    cloth_type=models.ForeignKey(ClothType,on_delete=models.CASCADE)

    class Meta:
        db_table='category_table'


class Dress(models.Model):
    dress_id=models.AutoField(primary_key=True)
    dress_name=models.CharField(max_length=100)
    dress_arrival=models.DateField(max_length=20)
    dress_price=models.IntegerField()
    cloth_type=models.ForeignKey(ClothType,on_delete=models.CASCADE)
    dress_img=models.ImageField(upload_to='dressimg/',blank=True, null=True)

    class Meta:
        db_table='dress'


class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    dress=models.ForeignKey(Dress,on_delete=models.CASCADE)

    class Meta:
        db_table='cart'
>>>>>>> 7cb7e58 (clothmate added)
