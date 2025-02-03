from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CaseEntry(models.Model):
    """ A case entered by user """
    case_no = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Case Entries "
    
    def __str__(self):
        """Return a string representation of the case no """
        return self.case_no
    
    
class CaseDetails(models.Model):
    """Specific details of the case """
    case_no = models.ForeignKey(CaseEntry,on_delete=models.CASCADE)
    description = models.TextField(default='not yet posted')
    judge = models.CharField(max_length=50)
    court_no = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Case Details"

    def __str__(self):
        return super().__str__()