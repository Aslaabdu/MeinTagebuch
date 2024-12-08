from app import app, db, User 


with app.app_context():
    
    user = User(username='Sena', password='Ecker', is_admin=False)

    
    db.session.add(user)
    db.session.commit()

    print("Benutzer wurde erfolgreich hinzugefügt!")
