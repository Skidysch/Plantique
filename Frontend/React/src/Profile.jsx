import React from "react";
import { Link, Outlet, useLoaderData } from "react-router-dom";

import "./styles/Profile.css";
import Button from "./components/Button";



export default function Profile() {
  const { user } = useLoaderData();

  return (
    <div className="profile">
      <div className="glass-bg"></div>
      <Outlet />
      <div className="profile__card">
        <div className="profile__card__left">
          <img
            className="profile__card__image"
            src={
              user.profile_picture
                ? `/${user.profile_picture}`
                : "/logo.svg"
            }
            alt="Profile picture"
          />
        </div>
        <div className="profile__card__right">
          <div className="profile__card__header">
            <h1 className="profile__card__name">Your profile</h1>
          </div>
          <div className="profile__card__info">
            <p className="profile__card__email">{`Username: ${user.username}`}</p>
            <p className="profile__card__email">{`Full name: ${
              user.full_name ? user.full_name : "Not set"
            }`}</p>
            <p className="profile__card__email">{`Email: ${user.email}`}</p>
            <p className="profile__card__gender">{`Gender: ${user.gender}`}</p>
            <p className="profile__card__birth-date">{`Birth date: ${
              user.birth_date ? user.birth_date : "Not set"
            }`}</p>
          </div>
          <div className="profile__card__action-buttons">
            <div className="profile__card__btn">
              <Link
                className="profile__card__btn__link"
                to={`/profile/edit/${user.id}`}
              >
                <Button content={"Edit profile"} />
              </Link>
            </div>
            <div className="profile__card__btn">
              <Link
                className="profile__card__btn__link"
                to={`/profile/delete/${user.id}`}
              >
                <Button content={"Delete profile"} />
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
