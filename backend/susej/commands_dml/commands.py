from susej.extension.database import db


def insert_table(table: object) -> None:
    db.session.add(table)
    db.session.commit()
    db.session.refresh(table)
    db.session.close()

def select_table(table: object) -> list:
    return table.query.all()

def delete_table(all=False, **args) -> None:
    if all:
        db.session.query(args['table']).delete()
    else:
        user_id = db.session.get(args['table'], id)
    
    db.session.commit()
    db.session.close()
    
def update_table() -> None:
    db.session.commit()
    db.session.close()
