import React, { useState } from "react";
import Button from "./Button";
import { Logo } from "./SVG";
import { Link } from "react-router-dom";

export default function HeaderMobile({scrollOpacity}) {
  const [isActive, setIsActive] = useState(false);

  const headerStyle = {
    backgroundColor: `rgba(0, 50, 0, ${scrollOpacity})`
  }

  const toggleActive = () => {
    setIsActive(!isActive);
    if (isActive) {
      document.body.style.overflow = 'auto';
    } else {
      document.body.style.overflow = 'hidden';
    }
  }

  const activeClass = isActive ? 'active' : '';

  const menuItems = [
    {name: 'Contact', link: '/contact'},
    {name: 'Blog', link: '/blog'},
    {name: 'Shop', link: '/shop'},
    {name: 'Log in', link: '/login'}
  ];

  return (
    <div className="header--mobile" style={headerStyle}>
      <ul className="header--mobile__list">
        <li className="header--mobile__logo" onClick={isActive ?? toggleActive}>
          <Link to={'/'}>
            <Button content={<Logo />} btnRound={true} size={60}/>
          </Link>
        </li>
        <nav className={"header--mobile__nav " + activeClass}>
          <ul className="header--mobile__nav__list">
            {menuItems.map((item, index) => {
              return <li key={index} className="header--mobile__nav__item" onClick={toggleActive}>
                <Link to={item.link} className="header__mobile__nav__link">
                  <Button content={item.name} btnHeader={true} />
                </Link>
              </li>
            })}
          </ul>
        </nav>
        <div className={"burger " + activeClass} onClick={toggleActive}>
          <div className="burger__top"></div>
          <div className="burger__main"></div>
          <div className="burger__bottom"></div>
        </div>
      </ul>
    </div>
  )
}