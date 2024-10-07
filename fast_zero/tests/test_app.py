from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange
    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    # client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'sousagomide',
            'email': 'sousagomide@gmail.com',
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'sousagomide',
        'email': 'sousagomide@gmail.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'sousagomide',
                'email': 'sousagomide@gmail.com'
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@gmail.com',
            'password': 'mynewpassword'
        }
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@gmail.com'
    }


def test_update_user_should_return_not_found(client):
    response = client.put(
        '/users/666',
        json={
            'username': 'bob',
            'email': 'bob@gmail.com',
            'password': 'mynewpassword'
        }
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_should_return_not_found(client):
    response = client.delete('/users/666')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_by_id_should_return_not_found(client):
    response = client.get('/users/666')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


# def test_get_user_by_id(client):
#     response = client.get('/users/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'username': 'bob',
#         'email': 'bob@gmail.com'
#     }
