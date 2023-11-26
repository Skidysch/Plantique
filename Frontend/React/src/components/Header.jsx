import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import Button from "./Button";
import { Logo, Search } from "./SVG";

export default function Header({ scrollOpacity}) {
  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`
  }
  
  return (
    <header className="header" style={headerStyle}>
      <ul className="header__list">
        <Link to="/">
          <li>
            <Button content={<Logo />} btnRound={true} size={60}/>
          </li>
        </Link>
        <li>
          <Button content='Contact' btnHeader={true}/>
        </li>
        <li>
          <Button content='Blog' btnHeader={true}/>
        </li>
      </ul>
      <ul className="header__list">
        <li>
          <Button content={<Search />} btnRound={true} size={60}/>
        </li>
        <li>
          <Button content='Shop' btnHeader={true}/>
        </li>
        <li>
          <Link to={'/login'}>
            <Button content='Log in' btnHeader={true}/>
          </Link>
        </li>
      </ul>
    </header>
  )
}