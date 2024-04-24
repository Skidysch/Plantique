import { useContext, useEffect } from "react";
import {
  Form,
  Link,
  useActionData,
  useNavigate,
} from "react-router-dom";
import Button from "./components/Button";
import { UserContext } from "./context/UserContext";

import "./styles/Auth.css";

const submitRegistration = async (data) => {
  const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: data.username,
      email: data.email,
      password: data.password,
    }),
  };

  const response = await fetch("/api/v1/users", requestOptions);
  const responseData = await response.json();

  if (!response.ok) {
    return { errorMessage: responseData.detail };
  } else {
    return {
      successMessage: "Registration successful",
      access_token: responseData.access_token,
    };
  }
};

export async function action({ request }) {
  const formData = await request.formData();

  const registerData = Object.fromEntries(formData);

  if (registerData.username.length < 3) {
    return { usernameError: "Username must be at least 3 characters" };
  }

  if (
    registerData.password === registerData.passwordRepeat &&
    registerData.password.length > 5
  ) {
    return await submitRegistration(registerData);
  } else {
    return {
      passwordError:
        "Make sure that passwords match and greater than 5 symbols",
    };
  }
}

export default function Register() {
  const data = useActionData();
  const { setToken } = useContext(UserContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (data?.access_token) {
      setToken(data.access_token);
      setTimeout(() => {
        navigate("/profile");
      }, 1000);
    }
  }, [data]);

  return (
    <div className="register">
      <div className="glass-bg"></div>
      <Form className="form" method="post" action="/register">
        <h1 className="form__title">Registration</h1>
        <div className="form__data">
          <label htmlFor="username" className="form__label">
            <input
              type="text"
              id="username"
              name="username"
              className="form__input"
              required
              placeholder="Username"
            />
          </label>
          {data?.usernameError && (
            <p className="form__error">{data.usernameError}</p>
          )}
          <label htmlFor="email" className="form__label">
            <input
              type="email"
              id="email"
              name="email"
              className="form__input"
              required
              placeholder="Email"
            />
          </label>
          <label htmlFor="password" className="form__label">
            <input
              type="password"
              id="password"
              name="password"
              className="form__input"
              required
              placeholder="Password"
            />
          </label>
          <label htmlFor="password-repeat" className="form__label">
            <input
              type="password"
              id="password-repeat"
              name="passwordRepeat"
              className="form__input"
              required
              placeholder="Repeat password"
            />
          </label>
          {data?.errorMessage && (
            <p className="form__error">{data.errorMessage}</p>
          )}
          {data?.passwordError && (
            <p className="form__error">{data.passwordError}</p>
          )}
          {data?.successMessage && (
            <p className="form__success">{data.successMessage}</p>
          )}
          <div className="form__btn" type="submit">
            <Button content={"Sign in"} btnDark={true} />
          </div>
        </div>
        <div className="register-forgot">
          <p>
            Already have an account?
            <br />
            <Link className="form__link" to={"/login"}>
              Log in
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
