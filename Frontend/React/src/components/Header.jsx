import React, { useContext, useEffect, useState } from "react";
import { Link, useLoaderData, useNavigate } from "react-router-dom";

import Button from "./Button";
import { Logo, Search } from "./SVG";
import { UserContext } from "../context/UserContext";

export default function Header({ scrollOpacity }) {
  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`,
  };

  const user = useLoaderData();

  const [username, setUsername] = useState(user.username);
  const [token, setToken] = useContext(UserContext);
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
              <Button content={username} btnHeader={true} />
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
