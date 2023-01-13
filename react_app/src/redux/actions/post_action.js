import axios from 'axios';
import * as ct from '../constants/constant'

export const getPosts = () => async (dispatch) => {//paramstring
    try {
        dispatch({ type: ct.POST.ACTION_TYPE.GET_POST_REQUEST });

        const { data } = await axios.get(ct.API_URL.ALL_POST);//?${paramstring}

        dispatch({
            type: ct.POST.ACTION_TYPE.GET_POST_SUCCESS,
            payload: data.data.list_data,
        });
    }
    catch (error) {
        dispatch({
            type: ct.POST.ACTION_TYPE.GET_POST_FAIL,
            payload: error
                // error.response && error.response.data.message
                //     ? error.response.data.message
                //     : error.message,
        });
    }
};