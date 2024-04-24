import React, { useContext, useEffect, useState } from "react";
import Button from "./Button";
import { Logo } from "./SVG";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";
import { getCurrentUser } from "../api/users";

export default function HeaderMobile({ scrollOpacity }) {
  const [isActive, setIsActive] = useState(false);
  const [profileIsActive, setProfileIsActive] = useState(false);

  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`,
  };

  const toggleActive = () => {
    setIsActive(!isActive);
    if (profileIsActive) {
      toggleProfileButton();
    }
    if (isActive) {
      document.body.style.overflow = "auto";
    } else {
      document.body.style.overflow = "hidden";
    }
  };

  const activeClass = isActive ? "active" : "";

  const { setToken, user } = useContext(UserContext);


  const pathname = useLocation().pathname;
  const navigate = useNavigate();

  const handleLogout = () => {
    setToken(null);
    navigate("/login");
  };

  const toggleProfileButton = () => {
    setProfileIsActive(!profileIsActive);
    const subList = document.querySelector(".header__profile__sublist--mobile");
    profileIsActive
      ? subList.classList.remove("header__profile__sublist--active")
      : subList.classList.add("header__profile__sublist--active");
  };

  return (
    <div id="header" className="header--mobile" style={headerStyle}>
      <ul className="header--mobile__list">
        <li
          className="header--mobile__logo"
          onClick={isActive ? toggleActive : undefined}
        >
          {pathname === "/" ? (
            <div
              onClick={() => {
                window.scrollTo({ top: 0, behavior: "smooth" });
              }}
            >
              <Button content={<Logo />} btnRound={true} size={60} />
            </div>
          ) : (
            <Link to="/">
              <Button content={<Logo />} btnRound={true} size={60} />
            </Link>
          )}
        </li>
        <nav className={"header--mobile__nav " + activeClass}>
          <ul className="header--mobile__nav__list">
            <li className="header--mobile__nav__item">
              <Button
                content="Contact"
                btnHeader={true}
                onClick={toggleActive}
              />
            </li>
            <li className="header--mobile__nav__item">
              <Button content="Blog" btnHeader={true} onClick={toggleActive} />
            </li>
            <li className="header--mobile__nav__item">
              <Button content="Shop" btnHeader={true} onClick={toggleActive} />
            </li>
            <li className="header--mobile__nav__item">
              {!user ? (
                <div onClick={toggleActive}>
                  <Link to={"/login"} className="header--mobile__nav__link">
                    <Button content={"Log in"} btnHeader={true} />
                  </Link>
                </div>
              ) : (
                <Button
                  content={user?.username}
                  btnHeader={true}
                  onClick={toggleProfileButton}
                />
              )}
            </li>
            <div
              className="header__profile__sublist--mobile"
              onClick={toggleActive}
            >
              <Link to={"/profile"}>
                <Button
                  content="Profile"
                  btnHeader={true}
                  onClick={toggleProfileButton}
                />
              </Link>
              <Link to={"/user/cart"}>
                <Button
                  content="Cart"
                  btnHeader={true}
                  onClick={toggleProfileButton}
                />
              </Link>
              <Link to={"/user/favorite"}>
                <Button
                  content="Favorite"
                  btnHeader={true}
                  btnDark={true}
                  onClick={toggleProfileButton}
                />
              </Link>
              <div onClick={toggleProfileButton}>
                <Button
                  content="Logout"
                  btnHeader={true}
                  onClick={handleLogout}
                />
              </div>
            </div>
          </ul>
        </nav>
        <div className={"burger " + activeClass} onClick={toggleActive}>
          <div className="burger__top"></div>
          <div className="burger__main"></div>
          <div className="burger__bottom"></div>
        </div>
      </ul>
    </div>
  );
}
