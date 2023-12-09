import React, { useContext, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

import Button from "./Button";
import { Logo, Search } from "./SVG";
import { UserContext } from "../context/UserContext";
import { getCurrentUser } from "../api/users";

export default function Header({ scrollOpacity }) {
  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`,
  };

  const { token, setToken, user, setUser } = useContext(UserContext);
  useEffect(() => {
    async function fetchUser() {
      const currentUser = await getCurrentUser();
      setUser(currentUser);
    }
    fetchUser();
  }, [])
  const navigate = useNavigate();

  const handleLogout = () => {
    setToken(null);
    navigate("/login");
  };

  return (
    <header className="header" style={headerStyle}>
      <ul className="header__list">
        <Link to="/">
          <li>
            <Button content={<Logo />} btnRound={true} size={60} />
          </li>
        </Link>
        <li>
          <Button content="Contact" btnHeader={true} />
        </li>
        <li>
          <Button content="Blog" btnHeader={true} />
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
