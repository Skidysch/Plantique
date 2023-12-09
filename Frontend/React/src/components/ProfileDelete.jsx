import React, { useContext, useEffect } from "react";
import Button from "./Button";
import { Form, useActionData, useNavigate, useParams } from "react-router-dom";
import { UserContext } from "../context/UserContext";

async function submitProfileDelete({ params }) {
  const requestOptions = {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  };

  const response = await fetch(`/api/users/${params.userId}`, requestOptions);
  const data = await response.json();
  console.log(data);

  if (!response.ok) {
    return { errorMessage: data.detail };
  } else {
    return { successMessage: "Profile deleted successfully" };
  }
}

export async function profileDeleteAction({ params }) {
  return await submitProfileDelete({ params });
}

export default function ProfileDelete() {
  const { setToken, setUser } = useContext(UserContext);
  const { userId } = useParams();
  const data = useActionData();
  const navigate = useNavigate();

  const cancelDelete = async () => {
    navigate("/profile");
  };

  useEffect(() => {
    if (data?.successMessage) {
      setToken(null);
      setUser(null);
      navigate("/");
      // setTimeout(() => {
      //   redirect("/");
      // }, 1000);
    }
  }, [data]);

  return (
    <div className="modal">
      <div className="modal__box">
        <h1 className="modal__title">Delete profile</h1>
        {/* not working with timed out redirect, find a way to to it */}
        {data && data?.successMessage && (
          <div className="form__success">{data.successMessage}</div>
        )}
        {data && data?.errorMessage && (
          <div className="form__error">Error: {data.errorMessage}</div>
        )}
        {!data && (
          <div className="modal__body">
            <p className="modal__text">
              Are you sure you want to delete this profile?
            </p>
            <div className="modal__buttons">
              <Form
                className="form form--invisible"
                method="post"
                action={`/profile/delete/${userId}`}
              >
                <Button content={"Yes"} />
              </Form>
              <Button content={"No"} onClick={cancelDelete} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
