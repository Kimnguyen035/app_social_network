import axios from "axios";
import * as ct from '../redux/constants/constant'

const login = (user) => {
    return axios
      .post(ct.API_URL.LOGIN, user)
      .then((response) => {
        if (response.data.accessToken) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }
  
        return response.data;
      });
  };