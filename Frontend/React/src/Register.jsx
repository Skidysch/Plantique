import { useContext, useEffect } from "react";
import { Form, Link, useActionData, useNavigate } from "react-router-dom";
import Button from "./components/Button";
import { UserContext } from "./context/UserContext";

import "./styles/Auth.css";
import instance from "./api/axios";

const submitRegistration = async (data) => {
  const requestData = JSON.stringify({
    username: data.username,
    email: data.email,
    password: data.password,
  });

  try {
    const registrationRes = await instance.post("/users", requestData, {
      headers: { "Content-Type": "application/json" },
    });

    if (registrationRes.status !== 201) {
      throw new Error("User registration failed");
    }

    const loginData = JSON.stringify(
      `grant_type=&username=${data.username}&password=${data.password}&scope=&client_id=&client_secret=`
    );

    const loginRes = await instance.post("/jwt/login", loginData, {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });

    return {
      successMessage: "Registration successful",
      accessToken: loginRes?.data.access_token,
    };
  } catch (err) {
    return {
      errorMessage: err.response?.data?.detail,
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
    const result = await submitRegistration(registerData);

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
    if (data?.status === "success") {
      localStorage.setItem("authToken", data.accessToken);
      setToken(data.accessToken);
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
          {data?.passwordError && (
            <p className="form__error">{data.passwordError}</p>
          )}
          {data?.errorMessage && (
            <p className="form__error">{data.errorMessage}</p>
          )}
          {data?.successMessage && (
            <p className="form__success">{data.successMessage}</p>
          )}
          <div className="form__btn">
            <Button content={"Sign in"} type="submit" btnDark={true} />
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
