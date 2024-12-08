from app import app, db, User 


with app.app_context():
    
    admin = User(username='Baki', password='Ecker', is_admin=True)

    
    db.session.add(admin)
    db.session.commit()

    print("Admin-Benutzer wurde erfolgreich hinzugefügt!")
