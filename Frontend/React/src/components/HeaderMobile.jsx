import React, { useContext, useEffect, useState } from "react";
import Button from "./Button";
import { Logo, Search } from "./SVG";
import { Link, useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";
import { getCurrentUser } from "../api/users";

export default function HeaderMobile({ scrollOpacity }) {
  const [isActive, setIsActive] = useState(false);

  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`,
  };

  const toggleActive = () => {
    setIsActive(!isActive);
    if (isActive) {
      document.body.style.overflow = "auto";
    } else {
      document.body.style.overflow = "hidden";
    }
  };

  const activeClass = isActive ? "active" : "";

  const { token, setToken, user, setUser } = useContext(UserContext);

  useEffect(() => {
    async function fetchUser() {
      const currentUser = await getCurrentUser();
      setUser(currentUser);
    }
    fetchUser();
  }, []);

  const navigate = useNavigate();

  const handleLogout = () => {
    setToken(null);
    navigate("/login");
  };

  return (
    <div className="header--mobile" style={headerStyle}>
      <ul className="header--mobile__list">
        <li className="header--mobile__logo" onClick={isActive ? toggleActive : undefined}>
          <Link to={"/"}>
            <Button content={<Logo />} btnRound={true} size={60} />
          </Link>
        </li>
        <nav className={"header--mobile__nav " + activeClass}>
          <ul className="header--mobile__nav__list">
            <li className="header--mobile__nav__item">
              <Button content="Contact" btnHeader={true} onClick={toggleActive}/>
            </li>
            <li className="header--mobile__nav__item">
              <Button content="Blog" btnHeader={true} onClick={toggleActive}/>
            </li>
            <li className="header--mobile__nav__item">
              <Button content="Shop" btnHeader={true} onClick={toggleActive}/>
            </li>
            {token && (
              <li className="header--mobile__nav__item">
                <Link to={"/profile"} className="header--mobile__nav__link">
                  <Button content={user.username} btnHeader={true} onClick={toggleActive}/>
                </Link>
              </li>
            )}
            <li className="header--mobile__nav__item" onClick={toggleActive}>
              {token === null ? (
                <Link to={"/login"} className="header--mobile__nav__link">
                  <Button content={"Log in"} btnHeader={true} />
                </Link>
              ) : (
                <Button
                  content="Logout"
                  onClick={handleLogout}
                  btnHeader={true}
                />
              )}
            </li>
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
