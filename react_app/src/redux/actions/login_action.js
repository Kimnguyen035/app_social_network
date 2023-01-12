import * as actionTypes from "../constants/login_constant";
import axios from "axios";

export const login = (user) => async (dispatch) => {
    try {
      dispatch({
        type: actionTypes.LOGIN_REQUEST,
        payload: user
      });

      const url = `${process.env.REACT_APP_API_URL}`;
  
      const { data } = await axios.post(url + 'login', user);
      
      dispatch({
        type: actionTypes.LOGIN_SUCCESS,
        payload: data
      });

      localStorage.setItem("tokens", JSON.stringify(data.data));
    } catch (error) {
      dispatch({
        type: actionTypes.LOGIN_FAIL,
        payload: error.message
      });
    }
  }