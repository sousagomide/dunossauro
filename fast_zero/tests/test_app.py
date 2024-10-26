from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange
    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}


# def test_update_user_should_return_not_found(client, token):
#     response = client.put(
#         '/users/666',
#         headers={'Authorization': f'Bearer {token}'},
#         json={
#             'username': 'bob',
#             'email': 'bob@gmail.com',
#             'password': 'mynewpassword'
#         }
#     )
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Usuário não encontrado'}


# def test_delete_user_should_return_not_found(client):
#     response = client.delete('/users/666')
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Usuário não encontrado'}


# def test_get_user_by_id_should_return_not_found(client):
#     response = client.get('/users/666')
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'Usuário não encontrado'}


# def test_get_user_by_id(client):
#     response = client.get('/users/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'username': 'bob',
#         'email': 'bob@gmail.com'
#     }
