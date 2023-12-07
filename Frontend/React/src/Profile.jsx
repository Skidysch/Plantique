import React from "react";
import { Link, useLoaderData } from "react-router-dom";

import { getCurrentUser } from "./api/users";
import "./styles/Profile.css";
import Button from "./components/Button";

export async function loader() {
  const user = await getCurrentUser();
  return user;
}

export default function Profile() {
  const currentUser = useLoaderData();
  console.log(currentUser);
  return (
    <div className="profile">
      <div className="profile__card">
        <div className="profile__card__left">
          <div className="profile__card__image">
            <img
              src={
                currentUser.profile_picture
                  ? currentUser.profile_picture
                  : '/profile-placeholder-image.png'
              }
              alt="Profile picture"
            />
          </div>
        </div>
        <div className="profile__card__right">
          <div className="profile__card__header">
            <h1 className="profile__card__name">
              Your profile
            </h1>
          </div>
          <div className="profile__card__info">
            <p className="profile__card__email">{`Username: ${currentUser.username}`}</p>
            <p className="profile__card__email">{`Full name: ${currentUser.full_name ? currentUser.full_name : 'Not set'}`}</p>
            <p className="profile__card__email">{`Email: ${currentUser.email}`}</p>
            <p className="profile__card__gender">{`Gender: ${currentUser.gender}`}</p>
            <p className="profile__card__birth-date">{`Birth date: ${currentUser.birth_date ? currentUser.birth_date : 'Not set'}`}</p>
          </div>
          <div className="profile__card__action-buttons">
            <div className="profile__card__btn">
              <Link className="profile__card__btn__link" to={"/profile/edit"}>
                <Button content={"Edit profile"} />
              </Link>
            </div>
            <div className="profile__card__btn">
              <Link className="profile__card__btn__link" to={"/profile/delete"}>
                <Button content={"Delete profile"} />
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
