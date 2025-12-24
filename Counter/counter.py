"""
Visitor count for ACG GCP Resume project
"""

from google.cloud import firestore
from flask import jsonify

def get_visitor_count():
    """
    Get and return the number of visitors
    """
    database = firestore.Client()
    counter_incr = 0
    visit_ref = database.collection(u'cloudresume').document(u'visitor_count')
    doc = visit_ref.get()
    if doc.exists:
        counter_incr = int(doc.to_dict()['count'])
    return counter_incr

def save_visit_data(counter_incr):
    """
    Saves the number of visitors to firestore
    """
    database = firestore.Client()
    visit_ref = database.collection(u'cloudresume').document(u'visitor_count')
    visit_ref.set({'count': counter_incr})

def visit_count(request):
    counter_incr = get_visitor_count()
    current_visitor = str(counter_incr + 1)
    save_visit_data(current_visitor)
    client_data = {
        'currentVisitor':  current_visitor
    }
    headers = {
        'Access-Control-Allow-Origin': '*'  #CORS for any origin
    }

return jsonify(client_data), 200, headers

