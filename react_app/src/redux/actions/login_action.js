import axios from "axios";
import * as ct from '../constants/constant'

export const login = (user) => async (dispatch) => {
    try {
      dispatch({
        type: ct.LOGIN.ACTION_TYPE.LOGIN_REQUEST,
        payload: user
      });
  
      const { data } = await axios.post(ct.API_URL.LOGIN, user);
      
      dispatch({
        type: ct.LOGIN.ACTION_TYPE.LOGIN_SUCCESS,
        payload: data
      });
    } catch (error) {
      dispatch({
        type: ct.LOGIN.ACTION_TYPE.LOGIN_FAIL,
        payload: error.message
      });
    }
  }