from django.db import models


class PortfolioChoices(models.TextChoices):
    """
    The  verification  for a particular potfolio
    """

    Frontend = ("frontend", "Frontend")
    Backend = ("backend", "Backend")
    Instructor = ("instructor", "Instructor")
    