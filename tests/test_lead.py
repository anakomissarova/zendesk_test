from datetime import datetime


def test_add_address_to_lead(app):
    lead_data = {'data': {'last_name': 'Johnson', 'organization_name': str(datetime.now())}}
    lead_id = app.lead.create(lead_data)['id']
    assert app.lead.exists(lead_id)
    address = {'address': {
        'line1': '2726 Smith Street',
        'city': 'Hyannis',
        'postal_code': '02601',
        'state': 'MA',
        'country': 'US'
    }}
    app.lead.modify(lead_id, address)
    new_lead_data = app.lead.get_lead(lead_id)
    assert address['address'] == new_lead_data['address']
