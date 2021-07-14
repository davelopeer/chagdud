from django import template
from django.template.defaultfilters import safe, linebreaks_filter

register = template.Library()

@register.simple_tag
def get_event_name_by_language(event, language):
  return event.get_name(language)

@register.simple_tag
def get_event_requirements_by_language(event, language):
  return event.get_requirements(language)

@register.simple_tag
def get_event_place_by_language(event, language):
  return event.get_place(language)

@register.simple_tag
def get_event_description_by_language(event, language):
  return linebreaks_filter(event.get_description(language))

@register.simple_tag
def get_event_short_description_by_language(event, language):
  return linebreaks_filter(event.get_short_description(language))

@register.simple_tag
def get_event_participation_text_by_language(event, language):
  return safe(event.get_participation_text(language))

@register.simple_tag
def get_event_policies_by_language(event, language):
  return safe(event.get_policies(language))
