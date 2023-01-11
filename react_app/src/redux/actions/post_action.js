import * as actionTypes from '../constants/post_constant';
import axios from 'axios';

export const getPosts = () => async (dispatch) => {//paramstring
    try {
        dispatch({ type: actionTypes.GET_POST_REQUEST });
        const url = `${process.env.REACT_APP_API_URL}`;

        const { data } = await axios.get(url + 'all-post');//?${paramstring}

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