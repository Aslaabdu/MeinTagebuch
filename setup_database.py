from app import app, db  

with app.app_context():
    db.create_all()  
    print("Tabellen wurden erfolgreich erstellt!")


#Löschen von Beiträgen
#DELETE FROM diary_entry WHERE id = 1;
#DELETE FROM diary_entry WHERE id = 2;