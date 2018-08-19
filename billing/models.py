# from django.db import models
# from django.conf import settings
# from django.db.models.signals import post_save, pre_save
#
# #User =
#
# #import stripe
# #stripe.api_key = 'sk_test_isI03GLVyjFFLxEIhsaRJlIh'
#
# class BillingProfileManager(models.Model):
#     def new_or_get(self, request):
#         user = request.user
#         guest_email_id = request.session.get('guest_email_id')
#         created = False
#         obj = None
#         if user.is_authenticated():
#             obj, created = self.model.objets.get_or_create(user=user, email=user.email)
#         elif guest_email_id is not None:
#             guest_email_obj = GuestEmail.objects.get_or_create(email=guest_email_obj.email)
#         else:
#             pass
#         return obj, created
#
#
# class BillingProfile(models.Model):
#     #user = models.OneToOneFiled(User, null=True, blank=True)
#     email = models.EmailField()
#     active = models.BooleanField(default=True)
#     update = models.DateTimeField(auto_now=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     customer_id = models.CharField(max_length=120, null=True, blank=True)  # customer id with stripe or braintree
#
#     objects = BillingProfileManager()
#
#     def __str__(self):
#         return self.email
#
#
# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
#     if not instance.customer_id and instance.email:
#         customer = stripe.Customer.create(email=instance.email)
#         instance.customer_id = newId
#
# pre_save.connect(billing_profile_created_receiver, sender=BillingProfile)
#
#
# def user_created_receiver(sender, instance, created, *args, **kwargs):
#     if created and instance.email:
#         BillingProfile.objects.get_or_create(user=instance, email=instance.email)
#
# post_save.connect(user_created_receiver, sender=User)


