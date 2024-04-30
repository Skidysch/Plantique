import { useContext } from "react";
import { Link, Outlet } from "react-router-dom";

import "./styles/ProfilePage.css";
import Button from "./components/Button";
import { UserContext } from "./context/UserContext";

export default function ProfilePage() {
  const { user } = useContext(UserContext);

  return (
    <div className="profile">
      <div className="glass-bg"></div>
      <Outlet />
      <div className="profile__card">
        <div className="profile__card__left">
          <img
            className="profile__card__image"
            src={
              user?.profile.profile_picture
                ? `/${user?.profile.profile_picture}`
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
            <p>{`Username: ${user?.username}`}</p>
            <p>{`First name: ${user?.profile.first_name || "Not set"}`}</p>
            <p>{`Last name: ${user?.profile.last_name || "Not set"}`}</p>
            <p>{`Email: ${user?.email}`}</p>
            <p>{`Birth date: ${user?.profile.birth_date || "Not set"}`}</p>
          </div>
          <div className="profile__card__action-buttons">
            <div className="profile__card__btn">
              <Link
                className="profile__card__btn__link"
                to={`/profile/edit/${user?.id}`}
              >
                <Button content={"Edit profile info"} />
              </Link>
            </div>
            <div className="profile__card__btn">
              <Link
                className="profile__card__btn__link"
                to={`/profile/edit/password/${user?.id}`}
              >
                <Button content={"Change password"} />
              </Link>
            </div>
            <div className="profile__card__btn">
              <Link
                className="profile__card__btn__link"
                to={`/profile/delete/${user?.id}`}
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
