import React, { useContext, useEffect, useState } from "react";
import Button from "./Button";
import { Form, useActionData, useNavigate, useParams } from "react-router-dom";
import { UserContext } from "../context/UserContext";

async function submitProfileEdit({ params, formData }) {
  const requestOptions = {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: formData.username,
      full_name: formData.fullName,
      email: formData.email,
      gender: formData.gender,
      password: formData.password,
      birth_date: formData.birthDate,
      profile_picture: formData.profilePicture,
    }),
  };

  const response = await fetch(`/api/users/${params.userId}`, requestOptions);
  const data = await response.json();

  if (!response.ok) {
    return { errorMessage: data.detail };
  } else {
    return { successMessage: "Profile edited successfully", user: data };
  }
}

export async function profileEditAction({ params, request }) {
  const formData = Object.fromEntries(await request.formData());

  let dataEntries = Object.entries(formData);

  dataEntries.forEach(([key, value]) => {
    if (value === "") {
      formData[key] = null;
    }
  });

  if (formData.password && formData.password.length > 5) {
    return await submitProfileEdit({ params, formData });
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

  return await submitProfileEdit({ params, formData });
}

export default function ProfileEdit() {
  const { setUser } = useContext(UserContext);
  const { userId } = useParams();
  const data = useActionData();
  const navigate = useNavigate();
  const [profilePicture, setProfilePicture] = useState("Profile picture");

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
        <h1 className="modal__title">Edit profile</h1>
        {/* not working with timed out redirect, find a way to to it */}
        {data && data?.successMessage && (
          <div className="form__success">{data.successMessage}</div>
        )}
        {(!data || data.errorMessage) && (
          <div className="modal__body">
            <Form
              className="form form--invisible"
              method="post"
              action={`/profile/edit/${userId}`}
            >
              <div className="form__data">
                <label htmlFor="username" className="form__label">
                  <input
                    type="text"
                    id="username"
                    name="username"
                    className="form__input"
                    placeholder="Username"
                  />
                </label>
                {data?.usernameError && (
                  <p className="form__error">{data.usernameError}</p>
                )}
                <label htmlFor="full-name" className="form__label">
                  <input
                    type="text"
                    id="full-name"
                    name="fullName"
                    className="form__input"
                    placeholder="Full name"
                  />
                </label>
                <label htmlFor="email" className="form__label">
                  <input
                    type="email"
                    id="email"
                    name="email"
                    className="form__input"
                    placeholder="Email"
                  />
                </label>
                <label htmlFor="gender" className="form__label">
                  <select
                    className="form__input"
                    id="gender"
                    name="gender"
                    defaultValue={""}
                  >
                    <option value="" disabled>
                      Gender
                    </option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                  </select>
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
                <label htmlFor="birth-date" className="form__label">
                  <input
                    type="date"
                    id="birth-date"
                    name="birthDate"
                    className="form__input"
                    placeholder="Birth date"
                  />
                </label>
                <label
                  htmlFor="profile-picture"
                  className="form__input form__label"
                >
                  {profilePicture}
                  <input
                    type="file"
                    id="profile-picture"
                    name="profilePicture"
                    style={{ display: "none" }}
                    onChange={(e) =>
                      setProfilePicture(`/${e.target.files[0].name}`)
                    }
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
