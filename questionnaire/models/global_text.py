from django.db import models


class GlobalText(models.Model):
    name = models.TextField(max_length=256, null=False, blank=False)
    question = models.TextField(max_length=256, null=True, blank=True, default='question')
    answer_this_part = models.TextField(max_length=1024, null=True, blank=True, default='answer this part')
    button_next = models.TextField(max_length=64, null=True, blank=True, default='Next')
    button_done = models.TextField(max_length=64, null=True, blank=True, default="I'm done!")
    button_previous_page = models.TextField(max_length=64, null=True, blank=True, default="Previous page")
    button_start_over = models.TextField(max_length=64, null=True, blank=True, default="Start over")
    survey_submitted = models.TextField(max_length=512, null=True, blank=True, default="Survey submitted")
    answers_have_been_saved = models.TextField(max_length=1024, null=True, blank=True, default="Thanks! Your answers have been saved") # noqa
    you_can_change_answers = models.TextField(max_length=1024, null=True, blank=True, default="You can always come back and change them.") # noqa

    class Meta:
        verbose_name = "global text"
        verbose_name_plural = "global texts"

    def __str__(self):
        return str(self.name)
