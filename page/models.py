from django.db import models

# Create your models here.


    

 
class Courses(models.Model):
    label = models.CharField(max_length=20,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2,default='FREE')
    date_creat = models.DateField(auto_now_add=True) 


    def __str__(self):
        return self.label
    

    
class Members(models.Model):
    Name = models.CharField(max_length=10,null=True)
    lName = models.CharField(max_length=10,null=True)
    Gob = models.CharField(max_length=20,blank=True,null=True,default='Develppeur')
    date_join = models.DateTimeField(auto_now=True)
    cours = models.ManyToManyField(Courses)


    
    
class MemberCourse():
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.Name} joined {self.course.label}"