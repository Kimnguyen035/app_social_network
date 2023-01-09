import * as actionTypes from "../constants/post_constant";

export const getPostReducer = (state = { posts: [] }, action) => {
  switch (action.type) {
    case actionTypes.GET_POST_REQUEST:
      return {
        loading: true,
        posts: [],
      };
    case actionTypes.GET_POST_SUCCESS:
      return {
        posts: action.payload,
        loading: false,
      };
    case actionTypes.GET_POST_FAIL:
      return {
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};