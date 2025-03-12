import requests


base_url = "https://yougile.com/api-v2"


def get_token(
        user='',
        password='SSS444-122sv',
        id_comp="d810d562-5ba4-410f-bc89-2615004000c4"
):
    creds = {
        'login': user,
        'password': password,
        'companyId': id_comp
        }
    resp = requests.post(base_url+'/auth/keys', json=creds)
    # return resp.json()["key"]


token = ""  # должно быть: 'token = get_token()', но у Юджайла закончились ключи
my_headers = {'Authorization': 'Bearer ' + token}


def create_project(name):
    project = {
            "title": name
     }
    resp = requests.post(base_url + '/projects',
                         json=project, headers=my_headers)
    return resp.json()


def update_project(name, new_id):
    project = {
            "title": name
     }
    resp = requests.put(base_url+f'/projects/{new_id}',
                         json=project, headers=my_headers)
    return resp.json()


def get_by_id(new_id):
    resp = requests.get(base_url+f'/projects/{new_id}', headers=my_headers)
    return resp.json()


def get_project_list():
    resp = requests.get(base_url + '/projects', headers=my_headers).json()["content"]
    return resp


def test_create_project_positive():
    body = get_project_list()
    len_before = len(body)

    create_project("11")

    body = get_project_list()
    len_after = len(body)
    assert len_after - len_before == 1


def test_create_project_negative():
    new_proj = create_project("")
    assert new_proj["statusCode"] == 400


def test_update_project_positive():
    title = "jkl11"
    result = create_project(title)
    new_id = result["id"]

    new_title = "jkl22"
    update_project(new_title, str(new_id))

    body = get_project_list()
    assert body[-1]["title"] == new_title


def test_update_project_negative():
    title = "jkl11"
    result = create_project(title)
    new_id = result["id"]

    new_title = ""
    update = update_project(new_title, str(new_id))

    assert update["message"] == ['title should not be empty']


def test_get_by_id():
    title = "12"
    result = create_project(title)
    new_id = result["id"]
    by_id = get_by_id(str(new_id))
    assert by_id["title"] == title
