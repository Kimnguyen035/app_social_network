import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';

import getPostReducer from './reducers/post_reducer'
import loginReducer from './reducers/login_reducer'


const reducer = combineReducers({
  post_list: getPostReducer,
  sigin: loginReducer
});

const middleware = [thunk];

const store = createStore(
  reducer,
  composeWithDevTools(applyMiddleware(...middleware))
);

export {store};
