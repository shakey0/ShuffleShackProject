from ShuffleShackApp.models.test_table import RunTable, db

def test_database_connection(test_app, test_client, seed_database):
    db.session.add(RunTable(name='second_record'))
    db.session.commit()

    result = RunTable.query.all()

    assert len(result) == 2
    assert result[0].name == 'first_record'
    assert result[1].name == 'second_record'
