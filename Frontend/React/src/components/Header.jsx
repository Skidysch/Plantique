import React, { useContext, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

import Button from "./Button";
import { Logo, Search } from "./SVG";
import { UserContext } from "../context/UserContext";
import { getCurrentUser } from "../api/users";

export default function Header({ scrollOpacity }) {
  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`,
  };

  const pathname = useLocation().pathname;
  const navigate = useNavigate();

  const { token, setToken, user, setUser } = useContext(UserContext);

  useEffect(() => {
    async function fetchUser() {
      const currentUser = await getCurrentUser();
      setUser(currentUser);
    }
    fetchUser();
  }, []);

  const handleLogout = () => {
    toggleProfileButton();
    setToken(null);
    navigate("/login");
  };

  const toggleProfileButton = () => {
    const subList = document.querySelector(".header__profile__sublist");
    subList.classList.toggle("header__profile__sublist--active");
  };

  return (
    <header id="header" className="header" style={headerStyle}>
      <ul className="header__list">
        <li>
          {pathname === "/" ? (
            <div onClick={() => {window.scrollTo({ top: 0, behavior: "smooth" })}}>
              <Button content={<Logo />} btnRound={true} size={60} />
            </div>
          ) : (
            <Link to="/">
              <Button content={<Logo />} btnRound={true} size={60} />
            </Link>
          )}
        </li>
        <li>
          <Link to="/contact">
            <Button content="Contact" btnHeader={true} />
          </Link>
        </li>
        <li>
          <Link to="/blog">
            <Button content="Blog" btnHeader={true} />
          </Link>
        </li>
      </ul>
      <ul className="header__list">
        <li>
          <Button content={<Search />} btnRound={true} size={60} />
        </li>
        <li>
          <Button content="Shop" btnHeader={true} />
        </li>
        {token && (
          <li>
            <Link to={"/profile"}>
              <Button content={user.username} btnHeader={true} />
            </Link>
          </li>
        )}
        <li>
          {token === null ? (
            <Link to={"/login"}>
              <Button content={"Log in"} btnHeader={true} />
            </Link>
          ) : (
            <Button content="Logout" onClick={handleLogout} btnHeader={true} />
          )}
        </li>
      </ul>
    </header>
  );
}
