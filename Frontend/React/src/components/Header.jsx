import React, { useEffect, useState } from "react";
import Button from "./Button";
import { Logo, Search } from "./SVG";

export default function Header({ scrollOpacity}) {
  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`
  }
  
  return (
    <div className="header" style={headerStyle}>
      <ul className="header__list">
        <a href="/">
          <li>
            <Button content={<Logo />} btnRound={true} size={60}/>
          </li>
        </a>
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
          <a href="#">
            <Button content='Log in' btnHeader={true}/>
          </a>
        </li>
      </ul>
    </div>
  )
}