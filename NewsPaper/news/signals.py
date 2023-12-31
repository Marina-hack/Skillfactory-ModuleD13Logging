from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory
from django.conf import settings


def send_notifications(preview, pk, title_post, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title_post,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def new_post_notification(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        # print(f'{subscribers = }')

        for category in categories:
            subscribers += category.subscribers.all()

            subscribers = [s.email for s in subscribers]
            # print(f'{subscribers = }')
            send_notifications(instance.preview(), instance.pk,
                               instance.title_post, subscribers)
