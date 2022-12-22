STATUS = { 
    'SUCCESS': 1,
    'NOT_LOGIN': 2,
    'NOT_PERMISSION': 3,
    'INPUT_INVALID': 4,
    'TOKEN_EXPIRED': 5,
    'NO_DATA': 6,
    'FAIL_REQUEST': 7
}

ERROR = {
    'wrong_password': 'Wrong password.',
    'not_exists': 'is not exists.',
    'exists': ' is exists',
    'refresh_token':'refresh_token is not exists.',
    'not_login':'Not logged in, token is null.',
    'token_not_exists':'Token is not exists.',
    'access_token':'Token fails, you can refresh token.',
    'user_exists': {
        'Username or email':'tai khoan da ton tai'
    },
    'user_exists_deleted': {
        'Username or email':'Tai khoan da ton tai, hay doi trang thai tai khoan'
    },
    'not_exists_user': 'User does not exist',
    'not_exists_post': 'Post does not exist.',
    'not_exists_trash': 'The post does not exist in the trash.',
    'not_exists_mail': 'This mail does not exist.',
    'send_mail_faild': 'Send mail failded.',
}

SUCCESS = {
    'login':'Login success.',
    'refresh_token':'Refresh success.',
    'create_post':'Post was created',
    'update_post':'Post was edited.',
    'deleted_post': 'Post was deleted',
    'restore_post': 'Post was restored',
    'drop_post': 'Post was dropped',
    'add_mail': 'Mail was saved',
    'edit_mail': 'Mail was edited',
    'send_mail': 'Mail was send',
}