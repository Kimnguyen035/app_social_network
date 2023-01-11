import React, { useState } from 'react'
import { useDispatch } from 'react-redux';
import './login.css'
import {login} from '../../redux/actions/login_action'

export default function Login() {
  const dispatch = useDispatch();

  const [username, setUsername] = useState('');
  const [password, setPassWord] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(login({username, password}));
  }
  return (
    <div className='login'>
      <div className='loginWrapper'>
        <div className='loginLeft'>
            <h3 className='loginLogo'>NewSocial</h3>
            <span className='loginDesc'>
                Connect with friends and the world around you on NewSocial
            </span>
        </div>
        <div className='loginRight'>
            <div className='loginBox'>
                <input placeholder='Username' id='username' className='loginInput' />
                <input placeholder='Password' type='password' id='password' className='loginInput' />
                <span class="material-icons">visibility</span>
                <button className='loginButton'>Log In</button>
                <span className='loginForgot'>Forgot Password?</span>
                <button className='loginRgisterButton'>
                    Create a new Account
                </button>
            </div>
        </div>
      </div>
    </div>
  )
}