import React, { useState } from "react";
import { Form } from "react-router-dom";
import Button from "./components/Button";

export async function action() {
  alert("log in");
}

export function Login() {  
  return (
    <div className="login">
      <Form className="login__form" method="post">
        <input type="text" className="login__input" placeholder="Username" />
        <input type="email" className="login__input" placeholder="Email" />
        <input type="password" className="login__input" placeholder="Password" />
        <div className="login__btn" type="submit">
          <Button content={'Log in'}
                  btnDark={true}
          />
        </div>
      </Form>
    </div>
  )
}