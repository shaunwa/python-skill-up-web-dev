from flask import Flask, request

app = Flask(__name__)

next_id = 5

contacts = [
    { 'id': '1', 'name': 'Shaun', 'phone': '123-234-3456' },
    { 'id': '2', 'name': 'Bob', 'phone': '234-234-3456' },
    { 'id': '3', 'name': 'Sue', 'phone': '345-234-3456' },
    { 'id': '4', 'name': 'Betty', 'phone': '567-234-3456' },
]

@app.get('/contacts')
def list_contacts():
    return contacts

@app.get('/contacts/<id>')
def read_single_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            return contact

    return 'That contact does not exist!'

@app.post('/contacts')
def create_contact():
    global next_id

    new_contact = {
        'id': f'{next_id}',
        'name': request.json['name'],
        'phone': request.json['phone'],
    }

    contacts.append(new_contact)

    next_id += 1

    return new_contact

@app.put('/contacts/<id>')
def update_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
            contact['phone'] = request.json['phone'] if 'phone' in request.json else contact['phone']
            return contact

    return 'There is no contact with that id!'

@app.delete('/contacts/<id>')
def delete_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contacts.remove(contact)
            return contact

    return 'There is no contact with that id!'

# GET /contacts - list
# GET /contacts/<id> - read
# POST /contacts - create
# PUT /contacts/<id> - update
# DELETE /contacts/<id> - delete

if __name__ == '__main__':
    app.run(debug=True)