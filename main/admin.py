from django.contrib import admin

from .models import (
    FAQ,
    Application,
    Award,
    Certification,
    Education,
    Introduction,
    Job,
    Opening,
    Organization,
    Patent,
    Profile,
    Publication,
    Resume,
    TeamMember,
    Testimonial,
    WorkExperience,
)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "job",
        "created_date",
    )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Opening)
class OpeningAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    pass


@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass
