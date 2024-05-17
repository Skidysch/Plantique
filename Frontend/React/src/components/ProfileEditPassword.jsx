import React, { useContext, useEffect, useState } from "react";
import Button from "./Button";
import { Form, useActionData, useNavigate, useParams } from "react-router-dom";
import { UserContext } from "../context/UserContext";
import instance from "../api/axios";

async function submitProfileEditPassword({ params, formData }) {
  const requestOptions = JSON.stringify({
    password: formData.password,
  });

  const response = await instance.patch(
    `/users/${params.userId}`,
    requestOptions
  );

  if (response.statusText !== "OK") {
    return { errorMessage: response.data.detail };
  } else {
    return { successMessage: "Password changed successfully", user: response.data };
  }
}

export async function profileEditPasswordAction({ params, request }) {
  const formData = Object.fromEntries(await request.formData());

  if (
    formData.password &&
    formData.repeatPassword &&
    formData.password !== formData.repeatPassword
  ) {
    return {
      passwordError: "Passwords does not match",
    };
  } else if (formData.password && formData.password.length > 5) {
    return await submitProfileEditPassword({ params, formData });
  } else if (
    formData.password &&
    formData.password.length > 0 &&
    formData.password.length <= 5
  ) {
    return {
      passwordError:
        "Make sure that passwords match and greater than 5 symbols",
    };
  }

  return await submitProfileEditPassword({ params, formData });
}

export default function ProfileEditPassword() {
  const { setUser } = useContext(UserContext);
  const { userId } = useParams();
  const data = useActionData();
  const navigate = useNavigate();

  const cancelEdit = async () => {
    navigate(-1);
  };

  useEffect(() => {
    if (data?.successMessage) {
      setUser(data.user);
      setTimeout(() => {
        navigate("/profile");
      }, 1000);
    }
  }, [data]);

  return (
    <div className="modal">
      <div className="modal__box">
        <h1 className="modal__title">Change password</h1>
        {/* not working with timed out redirect, find a way to to it */}
        {data && data?.successMessage && (
          <div className="form__success">{data.successMessage}</div>
        )}
        {(!data || data.errorMessage || data.passwordError) && (
          <div className="modal__body">
            <Form
              className="form form--invisible"
              method="post"
              action={`/profile/edit/password/${userId}`}
            >
              <div className="form__data">
                <label htmlFor="password" className="form__label">
                  <input
                    type="password"
                    id="password"
                    name="password"
                    className="form__input"
                    placeholder="Password"
                  />
                </label>
                <label htmlFor="repeat-password" className="form__label">
                  <input
                    type="password"
                    id="repeat-password"
                    name="repeatPassword"
                    className="form__input"
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
              </div>
              <div className="modal__buttons">
                <Button type={"submit"} content={"Save"} />
                <Button content={"Cancel"} onClick={cancelEdit} />
              </div>
            </Form>
          </div>
        )}
      </div>
    </div>
  );
}
