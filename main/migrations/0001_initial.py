# Generated by Django 4.0.3 on 2022-05-10 13:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import main.validators
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300, unique=True)),
                ('answer', models.TextField()),
                ('category', models.CharField(choices=[('category1', 'Category 1'), ('category2', 'Category 2')], max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=30)),
                ('job_description_file', models.FileField(blank=True, null=True, upload_to='resumes/%Y/%m/%d/', validators=[main.validators.validate_resume_file])),
                ('job_description_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=40, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/%Y/%m/%d/', validators=[main.validators.validate_resume_file])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='team/photos/%Y/%m/%d/', validators=[main.validators.validate_image_file])),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('company', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('is_current', models.BooleanField(default=True)),
                ('end_date', models.DateField()),
                ('description', models.TextField(max_length=1000)),
                ('company_url', models.URLField()),
                ('employment_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract/Consultancy'), ('internship', 'Internship')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('publication_publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('publication_url', models.URLField(blank=True, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_publications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('phone_number', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=200)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/%Y/%m/%d/', validators=[main.validators.validate_resume_file])),
                ('timezone', models.IntegerField(choices=[(-3, 'UTC-3'), (-2, 'UTC-2'), (-1, 'UTC-1'), (0, 'UTC'), (1, 'UTC+1'), (2, 'UTC+2'), (3, 'UTC+3')])),
                ('availability', models.IntegerField(choices=[(1, 'Immediate'), (2, 'Less than 2 weeks'), (3, ' Less than 4 weeks,'), (4, 'More than 4 weeks')])),
                ('contact_future_opportunities', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='team/photos/%Y/%m/%d/', validators=[main.validators.validate_image_file])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_title', models.CharField(max_length=300, unique=True)),
                ('patent_office', models.CharField(max_length=100, unique=True)),
                ('patent_url', models.URLField()),
                ('patent_number', models.CharField(max_length=100, unique=True)),
                ('patent_state', models.CharField(choices=[('issued', 'Issued'), ('pending', 'Pending')], max_length=50)),
                ('patent_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_patents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='organizations/logos/%Y/%m/%d/', validators=[main.validators.validate_image_file])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, max_length=250)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_organizations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('industry', models.CharField(choices=[('advertising_media_communications', 'Advertising, Media & Communications'), ('agriculture_fishing_forestry', 'Agriculture, Fishing & Forestry'), ('automotive_aviation', 'Automotive & Aviation'), ('banking_finance_insurance', 'Banking, Finance & Insurance'), ('construction', 'Construction'), ('energy_utilities', 'Energy & Utilities'), ('enforcement_security', 'Enforcement & Security'), ('government', 'Government'), ('healthcare', 'Healthcare'), ('hospitality_hotel', 'Hospitality & Hotel'), ('it_telecoms', 'IT & Telecoms'), ('law_compliance', 'Law & Compliance'), ('manufacturing_warehousing', 'Manufacturing & Warehousing'), ('ngo_npo_charity', 'NGO, NPO & Charity'), ('recruitment', 'Recruitment'), ('retail_fashion_fmcg', 'Retail, Fashion & FMCG'), ('shipping_logistics', 'Shipping & Logistics'), ('tourism_travel', 'Tourism & Travel')], max_length=50)),
                ('functions', models.CharField(choices=[('quality_assurance', 'Quality Assurance'), ('product', 'Product Management'), ('devops', 'DevOps'), ('design', 'Product & UI/UX Design'), ('software_engineering', 'Software Engineering'), ('architect', 'Archictect')], max_length=50)),
                ('type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract/Consultancy'), ('internship', 'Internship')], max_length=20)),
                ('level', models.IntegerField(choices=[(1, 'Entry Level'), (2, 'Intermediate'), (3, 'Mid-Level'), (4, 'Senior or executive-level')])),
                ('timezone', models.IntegerField(choices=[(-3, 'UTC-3'), (-2, 'UTC-2'), (-1, 'UTC-1'), (0, 'UTC'), (1, 'UTC+1'), (2, 'UTC+2'), (3, 'UTC+3')])),
                ('description', ckeditor.fields.RichTextField()),
                ('min_salary', models.IntegerField(blank=True, default=0)),
                ('max_salary', models.IntegerField(blank=True, default=0)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('is_closed', models.BooleanField(default=False, editable=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_jobs', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_jobs', to='main.organization')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['deadline', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_introduction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_university', models.CharField(max_length=100)),
                ('field_of_study', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('grade', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('is_current', models.BooleanField(default=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('school_website_url', models.URLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_educations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('issuer', models.CharField(max_length=100)),
                ('will_expire', models.BooleanField(default=True)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('credential_id', models.CharField(blank=True, max_length=100, null=True)),
                ('credential_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_certifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('issuer', models.CharField(max_length=100)),
                ('issue_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('associated_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_awards', to='main.workexperience')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_awards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone_number', models.CharField(max_length=40)),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Rejected'), (3, 'Set up interview'), (4, 'Approved'), (5, 'On Hold'), (6, 'Cancelled')], default=1)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/%Y/%m/%d/', validators=[main.validators.validate_resume_file])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='main.job')),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
    ]
