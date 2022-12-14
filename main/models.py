from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_countries.fields import CountryField
from taggit.managers import TaggableManager

from accounts.models import User

from .validators import validate_image_file, validate_resume_file

# Create your models here.
FUNCTION_CHOICES = [
    ("quality_assurance", "Quality Assurance"),
    ("product", "Product Management"),
    ("devops", "DevOps"),
    ("design", "Product & UI/UX Design"),
    ("software_engineering", "Software Engineering"),
    ("architect", "Archictect"),
]

INDUSTRY_CHOICES = [
    ("advertising_media_communications", "Advertising, Media & Communications"),
    ("agriculture_fishing_forestry", "Agriculture, Fishing & Forestry"),
    ("automotive_aviation", "Automotive & Aviation"),
    ("banking_finance_insurance", "Banking, Finance & Insurance"),
    ("construction", "Construction"),
    ("energy_utilities", "Energy & Utilities"),
    ("enforcement_security", "Enforcement & Security"),
    ("government", "Government"),
    ("healthcare", "Healthcare"),
    ("hospitality_hotel", "Hospitality & Hotel"),
    ("it_telecoms", "IT & Telecoms"),
    ("law_compliance", "Law & Compliance"),
    ("manufacturing_warehousing", "Manufacturing & Warehousing"),
    ("ngo_npo_charity", "NGO, NPO & Charity"),
    ("recruitment", "Recruitment"),
    ("retail_fashion_fmcg", "Retail, Fashion & FMCG"),
    ("shipping_logistics", "Shipping & Logistics"),
    ("tourism_travel", "Tourism & Travel"),
]

TYPE_CHOICES = [
    ("full_time", "Full-time"),
    ("part_time", "Part-time"),
    ("contract", "Contract/Consultancy"),
    ("internship", "Internship"),
]

LEVEL_CHOICES = [
    (1, "Entry Level"),
    (2, "Intermediate"),
    (3, "Mid-Level"),
    (4, "Senior or executive-level"),
]

TIME_ZONE_CHOICES = [
    (-3, "UTC-3"),
    (-2, "UTC-2"),
    (-1, "UTC-1"),
    (0, "UTC"),
    (1, "UTC+1"),
    (2, "UTC+2"),
    (3, "UTC+3"),
]


# Note: Placeholder categories to be changed later
FAQ_CATEGORY_CHOICES = [
    ("category1", "Category 1"),
    ("category2", "Category 2"),
]


AVAILABILITY_CHOICES = [
    (1, "Immediate"),
    (2, "Less than 2 weeks"),
    (3, " Less than 4 weeks,"),
    (4, "More than 4 weeks"),
]


PATENT_CHOICES = [
    ("issued", "Issued"),
    ("pending", "Pending"),
]


class Organization(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(
        upload_to="organizations/logos/%Y/%m/%d/",
        blank=True,
        null=True,
        validators=[validate_image_file],
    )

    # meta fields:
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_organizations"
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(max_length=250, editable=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            qs = Organization.objects.filter(slug=self.slug)
            if qs.exists():
                self.slug = "{}-{}".format(self.slug, len(qs))
        super(Organization, self).save(*args, **kwargs)


class Job(models.Model):
    title = models.CharField(max_length=200)
    industry = models.CharField(choices=INDUSTRY_CHOICES, max_length=50)
    functions = models.CharField(max_length=50, choices=FUNCTION_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    timezone = models.IntegerField(choices=TIME_ZONE_CHOICES)
    description = RichTextField()
    min_salary = models.IntegerField(default=0, blank=True)
    max_salary = models.IntegerField(default=0, blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    # System generated fields:
    is_closed = models.BooleanField(default=False, editable=False)
    # Meta fields
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_jobs"
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="organization_jobs"
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, editable=False, unique=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "view_job",
            kwargs={
                "pk": self.pk,
                "slug": self.slug,
            },
        )

    class Meta:
        ordering = ["deadline", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            qs = Job.objects.filter(slug=self.slug)
            if qs.exists():
                self.slug = "{}-{}".format(self.slug, len(qs))
        super(Job, self).save(*args, **kwargs)


class Application(models.Model):
    STATUS_CHOICES = (
        (1, "New"),
        (2, "Rejected"),
        (3, "Set up interview"),
        (4, "Approved"),
        (5, "On Hold"),
        (6, "Cancelled"),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    country = CountryField()
    phone_number = models.CharField(max_length=40)
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="job_applications"
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    resume = models.FileField(
        upload_to="resumes/%Y/%m/%d/",
        blank=True,
        null=True,
        validators=[validate_resume_file],
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ("created_date",)


class Resume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_number = models.CharField(max_length=40, blank=True, null=True)
    resume = models.FileField(
        upload_to="resumes/%Y/%m/%d/",
        blank=True,
        null=True,
        validators=[validate_resume_file],
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ("created_date",)


class Opening(models.Model):
    organization_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email_address = models.EmailField()
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    job_description_file = models.FileField(
        upload_to="resumes/%Y/%m/%d/",
        blank=True,
        null=True,
        validators=[validate_resume_file],
    )
    job_description_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.organization_name


class Testimonial(models.Model):
    testimonial = models.TextField()
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)


def __str__(self):
    return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to="team/photos/%Y/%m/%d/",
        validators=[validate_image_file],
    )
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school_university = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    grade = models.CharField(blank=True, null=True, max_length=100)
    start_date = models.DateField()
    is_current = models.BooleanField(default=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    school_website_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_educations"
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.school_university


class Introduction(models.Model):
    summary = models.TextField()
    created_by = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_introduction"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary


class FAQ(models.Model):
    question = models.CharField(max_length=300, unique=True)
    answer = models.TextField()
    category = models.CharField(max_length=100, choices=FAQ_CATEGORY_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.question


class Patent(models.Model):
    patent_title = models.CharField(max_length=300, unique=True)
    patent_office = models.CharField(max_length=100, unique=True)
    patent_url = models.URLField()
    patent_number = models.CharField(unique=True, max_length=100)
    patent_state = models.CharField(max_length=50, choices=PATENT_CHOICES)
    patent_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_patents"
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.patent_title


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    city = models.CharField(max_length=200)
    resume = models.FileField(
        upload_to="resumes/%Y/%m/%d/",
        blank=True,
        null=True,
        validators=[validate_resume_file],
    )
    timezone = models.IntegerField(choices=TIME_ZONE_CHOICES)
    availability = models.IntegerField(choices=AVAILABILITY_CHOICES)
    contact_future_opportunities = models.BooleanField(default=True)
    photo = models.ImageField(
        upload_to="team/photos/%Y/%m/%d/",
        validators=[validate_image_file],
    )
    created_by = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=300)
    publication_publisher = models.CharField(max_length=100, null=True, blank=True)
    publication_url = models.URLField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_publications"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    title = models.CharField(max_length=300)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    is_current = models.BooleanField(default=True)
    end_date = models.DateField()
    description = models.TextField(max_length=1000)
    company_url = models.URLField()
    employment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_experiences"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    will_expire = models.BooleanField(default=True)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(null=True, blank=True, max_length=100)
    credential_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_certifications"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Award(models.Model):
    title = models.CharField(max_length=100)
    associated_with = models.ForeignKey(
        WorkExperience, on_delete=models.CASCADE, related_name="experience_awards"
    )
    issuer = models.CharField(max_length=100)
    issue_date = models.DateTimeField()
    description = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_awards"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
