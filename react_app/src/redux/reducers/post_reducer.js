import * as ct from '../constants/constant'

const initialState = {
  posts:[],
  loading:false,
  errorMessage:''
}    

const getPostReducer = (state = initialState, action) => {
  switch (action.type) {
    case ct.POST.ACTION_TYPE.GET_POST_REQUEST:
      return {
        loading: true,
        posts: [],
      };
    case ct.POST.ACTION_TYPE.GET_POST_SUCCESS://actionTypes.GET_POST_SUCCESS:
      return {
        posts: action.payload,
        loading: false,
      };
    case ct.POST.GET_POST_FAIL:
      return {
        loading: false, 
        error: action.payload,
      };  
    default:
      return state;
  }
};

export default getPostReducer