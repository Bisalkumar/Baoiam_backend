from django.db import models

# Create your models here.


class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Web Development', 'Web Development'),
        ('Data Analyst', 'Data Analyst'),
        ('Data Science', 'Data Science'),
        ('Content Writing', 'Content Writing'),
        ('Graphic Designing', 'Graphic Designing'),
        ('SEO Marketing', 'SEO Marketing'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Project Management', 'Project Management'),
        ('Human Resources', 'Human Resources'),
        ('Corporation', 'Corporation'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Web Development')
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=50)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    status_choices = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('draft', 'Draft'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
