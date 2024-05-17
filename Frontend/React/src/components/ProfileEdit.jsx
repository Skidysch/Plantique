import React, { useContext, useEffect, useState } from "react";
import Button from "./Button";
import { Form, useActionData, useNavigate, useParams } from "react-router-dom";
import { UserContext } from "../context/UserContext";
import instance from "../api/axios";

async function submitProfileEdit({ params, formData }) {
  const convertKeysToSnakeCase = (obj) => {
    const snakeCaseObj = {};
    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        const snakeCaseKey = key.replace(
          /[A-Z]/g,
          (match) => `_${match.toLowerCase()}`
        );
        snakeCaseObj[snakeCaseKey] = obj[key];
      }
    }
    return snakeCaseObj;
  };

  const filteredFormData = Object.fromEntries(
    Object.entries(formData).filter(([_, value]) => value !== "")
  );

  const apiFormData = convertKeysToSnakeCase(filteredFormData);

  const requestOptions = JSON.stringify(apiFormData)

  const response = await instance.patch(
    `/profiles/${params.userId}`,
    requestOptions
  );

  if (response.statusText !== "OK") {
    return { errorMessage: response.data.detail };
  } else {
    return { successMessage: "Profile edited successfully", user_profile: response.data };
  }
}

export async function profileEditAction({ params, request }) {
  const formData = Object.fromEntries(await request.formData());
  return await submitProfileEdit({ params, formData });
}

export default function ProfileEdit() {
  const {user, setUser } = useContext(UserContext);
  const { userId } = useParams();
  const data = useActionData();
  const navigate = useNavigate();
  const [profilePicture, setProfilePicture] = useState("Profile picture");

  const cancelEdit = async () => {
    navigate(-1);
  };

  useEffect(() => {
    if (data?.user_profile) {
      setUser({...user, profile: data.user_profile});
      
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
                <label htmlFor="first-name" className="form__label">
                  <input
                    type="text"
                    id="first-name"
                    name="firstName"
                    className="form__input"
                    placeholder="First name"
                  />
                </label>
                <label htmlFor="last-name" className="form__label">
                  <input
                    type="text"
                    id="last-name"
                    name="lastName"
                    className="form__input"
                    placeholder="Last name"
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
