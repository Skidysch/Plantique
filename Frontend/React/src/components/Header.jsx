import { useContext } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

import Button from "./Button";
import { Logo, Search } from "./SVG";
import { UserContext } from "../context/UserContext";

export default function Header({ scrollOpacity }) {
  const { token, setToken, user } = useContext(UserContext);

  const pathname = useLocation().pathname;
  const navigate = useNavigate();

  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`,
  };

  const handleLogout = () => {
    toggleProfileButton();
    localStorage.setItem("authToken", null);
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
        <li>
          {!user ? (
            <Link to={"/login"}>
              <Button content={"Log in"} btnHeader={true} />
            </Link>
          ) : (
            <Button
              content={user.username}
              btnHeader={true}
              onClick={toggleProfileButton}
            />
          )}
        </li>
      </ul>
      <div className="header__profile__sublist">
        <Link to={"/profile"}>
          <Button
            content="Profile"
            btnHeader={true}
            btnDark={true}
            onClick={toggleProfileButton}
          />
        </Link>
        <Link to={"/user/cart"}>
          <Button
            content="Cart"
            btnHeader={true}
            btnDark={true}
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
        <Button
          content="Logout"
          btnHeader={true}
          btnDark={true}
          onClick={handleLogout}
        />
      </div>
    </header>
  );
}
