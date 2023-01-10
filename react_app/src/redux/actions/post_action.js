import * as actionTypes from '../constants/post_constant';
import axios from 'axios';

export const getPosts = () => async (dispatch) => {//paramstring
    try {
        dispatch({ type: actionTypes.GET_POST_REQUEST });

        const { data } = await axios.get(`http://127.0.0.1:8000/all-post`);//?${paramstring}

        dispatch({
            type: actionTypes.GET_POST_SUCCESS,
            payload: data.data.list_data,
        });
    }
    catch (error) {
        dispatch({
            type: actionTypes.GET_POST_FAIL,
            payload: error
                // error.response && error.response.data.message
                //     ? error.response.data.message
                //     : error.message,
        });
    }
};