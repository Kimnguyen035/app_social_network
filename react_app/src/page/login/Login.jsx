import React, { useState } from 'react'
import { useDispatch } from 'react-redux';
import './login.css'
import {login} from '../../redux/actions/login_action'

export default function Login() {
  const dispatch = useDispatch();

  const [username, setUsername] = useState('')
  const [password, setPassWord] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    dispatch(login({username, password}))
    
    // console.log(u)
    // history.push(`/cart`);
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
                <input className='loginInput' placeholder='Username' onChange={(e) => setUsername(e.target.value)} />
                <input className='loginInput' placeholder='Password' type='password' onChange={(e) => setPassWord(e.target.value)} />
                <span class="material-icons">visibility</span>
                <button className='loginButton' onClick={handleSubmit}>Log In</button>
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