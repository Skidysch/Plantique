import React, { useContext, useEffect, useState } from "react";
import { Form, Link, redirect, useActionData, useNavigate } from "react-router-dom";
import Button from "./components/Button";

import "./styles/Auth.css";
import { UserContext } from "./context/UserContext";

const submitLogin = async (data) => {
  const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: JSON.stringify(
      `grant_type=&username=${data.email}&password=${data.password}&scope=&client_id=&client_secret=`
    ),
  };

  const response = await fetch("/api/token", requestOptions);
  const responseData = await response.json();

  if (!response.ok) {
    return { errorMessage: responseData.detail };
  } else {
    return {
      successMessage: "Successfuly logged in",
      token: responseData.access_token,
    };
  }
};

export async function action({ request }) {
  const formData = await request.formData();
  const loginData = Object.fromEntries(formData);

  return await submitLogin(loginData);
}

export default function Login() {
  const data = useActionData();
  const [, setToken] = useContext(UserContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (data?.successMessage) {
      setToken(data.token);
      setTimeout(() => {
        navigate("/profile");
      }, 1000);
    }
  }, [data]);

  return (
    <div className="login">
      <Form className="form" method="post" action="/login">
        <h1 className="form__title">Authorization</h1>
        <div className="form__data">
          <label htmlFor="email" className="form__label">
            <input
              type="email"
              id="email"
              name="email"
              className="form__input"
              placeholder="Email"
            />
          </label>
          <label htmlFor="password" className="form__label">
            <input
              type="password"
              id="password"
              name="password"
              className="form__input"
              placeholder="Password"
            />
          </label>
          {data?.successMessage && (
            <p className="form__success">{data.successMessage}</p>
          )}
          {data?.errorMessage && (
            <p className="form__error">{data.errorMessage}</p>
          )}
          <div className="form__btn" type="submit">
            <Button content={"Log in"} btnDark={true} />
          </div>
        </div>
        <div className="register-forgot">
          <p>
            Don't have an account?
            <br />
            <Link className="form__link" to={"/register"}>
              Register
            </Link>
          </p>
          <p>
            Forgot your password?
            <br />
            <Link className="form__link" to={"/restore"}>
              Restore
            </Link>
          </p>
        </div>
      </Form>
    </div>
  );
}
