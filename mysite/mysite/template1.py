import datetime
from django.http import HttpResponse
from django.http import HttpResponse, request
from django.template import Template,Context


def template(request):
    raw_template="""
    <p>Dear {{ person_name }},
    <p>Thanks for ordering {{ product }} from {{ company }}. It's scheduled to ship on {{ ship_date|date:"F j, Y" }}.</p>

    {% if ordered_warranty %}
    <p>Your warranty information will be included in the packaging.</p>
    {% endif %}

    <p>Sincerely,<br />{{ company }}</p>
    """
    t=Template(raw_template)
    c=Context({'person_name': 'John Smith',
    'product': 'Super Lawn Mower',
    'company': 'Outdoor Equipment',
    'ship_date': datetime.date(2009, 4, 2),
    'ordered_warranty': True})
    
    return HttpResponse(t.render(c))