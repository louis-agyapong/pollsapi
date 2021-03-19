from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    question = models.CharField(_("question"), max_length=100)
    created_by = models.ForeignKey(User, verbose_name=_("created by"), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(_("published date"), auto_now=True)

    class Meta:
        verbose_name = _("poll")
        verbose_name_plural = _("polls")

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, verbose_name=_("poll"), related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(_("choice text"), max_length=100)

    class Meta:
        verbose_name = _("choice")
        verbose_name_plural = _("choices")

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, verbose_name=_("choice"), related_name="votes", on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, verbose_name=_("poll"), on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, verbose_name=_("voted by"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("vote")
        verbose_name_plural = _("votes")
        unique_together = ("poll", "voted_by")

    def __str__(self) -> str:
        return str(self.choice)
