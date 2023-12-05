import React from "react";
import { Form, Link, redirect } from "react-router-dom";
import Button from "./components/Button";

import './styles/Auth.css';

export async function action() {
  alert("log in");
  return redirect('/');
}

export function Login() {
  return (
    <div className="login">
      <Form className="form" method="post">
        <div className="form__data">
          <input type="email" className="form__input" placeholder="Email" />
          <input type="password" className="form__input" placeholder="Password" />
          <div className="form__btn" type="submit">
            <Button content={'Log in'}
                    btnDark={true}
            />
          </div>
        </div>
        <div className="register-forgot">
          <p>
            Don't have an account?<br/>
            <Link className="form__link" to={'/register'}>Register</Link>
          </p>
          <p>
            Forgot your password?<br/>
            <Link className="form__link" to={'/forgot'}>Restore</Link>
          </p>
        </div>
      </Form>
    </div>
  )
}