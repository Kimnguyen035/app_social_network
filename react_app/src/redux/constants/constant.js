const API_URL = {
    'ALL_POST': `${process.env.REACT_APP_API_URL}all-post`,
    'LOGIN': `${process.env.REACT_APP_API_URL}login`,
}

const POST = {
    'ACTION_TYPE': {
        'GET_POST_REQUEST': 'GET_POST_REQUEST',
        'GET_POST_SUCCESS': 'GET_POST_SUCCESS',
        'GET_POST_FAIL': 'GET_POST_FAIL',
    }
}

const LOGIN = {
    'ACTION_TYPE': {
        'LOGIN_REQUEST': 'LOGIN_REQUEST',
        'LOGIN_SUCCESS': 'LOGIN_SUCCESS',
        'LOGIN_FAIL': 'LOGIN_FAIL',
    }
}

export {API_URL, POST, LOGIN}