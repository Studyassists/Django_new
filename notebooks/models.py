from secrets import token_urlsafe
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    profile_image = models.ImageField(
        upload_to='profiles/', blank=True, null=True
    )

    def __str__(self):
        return f"Profile of {self.user.email}"


class UserDocument(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='documents'
    )
    filename = models.CharField(max_length=255)
    persist_dir = models.CharField(max_length=500)
    summary = models.TextField(blank=True, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'filename')
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.user.email} — {self.filename}"


class EmailVerificationToken(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='email_verification'
    )
    token = models.CharField(max_length=64, unique=True, default=token_urlsafe)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Verification token for {self.user.email}"
