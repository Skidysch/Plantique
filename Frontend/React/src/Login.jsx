import { useContext, useEffect } from "react";
import { Form, Link, useActionData, useNavigate } from "react-router-dom";
import Button from "./components/Button";

import "./styles/Auth.css";
import { UserContext } from "./context/UserContext";
import instance from "./api/axios";

const submitLogin = async (data) => {
  const requestData = JSON.stringify(
    `grant_type=&username=${data.username}&password=${data.password}&scope=&client_id=&client_secret=`
  );

  try {
    const res = await instance.post("/jwt/login", requestData, {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });
    return {
      successMessage: "Successfully logged in",
      accessToken: res.data.access_token,
    };
  } catch (err) {
    return {
      errorMessage: err.response?.data?.detail,
    };
  }
};

export async function action({ request }) {
  const formData = await request.formData();
  const loginData = Object.fromEntries(formData);

  const result = await submitLogin(loginData);

  if (result.errorMessage) {
    return {
      status: "error",
      errorMessage: result.errorMessage,
    };
  } else {
    return {
      status: "success",
      successMessage: result.successMessage,
      accessToken: result.accessToken,
    };
  }
}

export default function Login() {
  const data = useActionData();
  const { setToken } = useContext(UserContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (data?.status === "success") {
      localStorage.setItem("authToken", data.accessToken);
      setToken(data.accessToken);
      setTimeout(() => {
        navigate("/profile");
      }, 1000);
    }
  }, [data]);

  return (
    <div className="login">
      <div className="glass-bg"></div>
      <Form className="form" method="post" action="/login">
        <h1 className="form__title">Authorization</h1>
        <div className="form__data">
          <label htmlFor="username" className="form__label">
            <input
              type="username"
              id="username"
              name="username"
              className="form__input"
              placeholder="Username"
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
          <div className="form__btn">
            <Button content={"Log in"} type="submit" btnDark={true} />
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
