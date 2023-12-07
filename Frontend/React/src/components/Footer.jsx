import React from "react";
import FooterLogo from "/footer-logo.png";
import SocialList from "./SocialList";

export default function Footer() {
  return (
    <footer className="footer">
      <img src={FooterLogo} alt="Footer logo" className="footer__logo" />
      <h3 className="footer__title">Join the Community!</h3>
      <p className="footer__description">
        Subscribe to The Forager to receive monthly plant tips, store updates,
        promotions & more
      </p>
      <div className="footer__bottom">
        <div className="footer__social">
          <SocialList />
        </div>
        <div className="footer__sep"></div>
        <p className="footer__copy">©2023, All Right Reserved.</p>
      </div>
    </footer>
  );
}
