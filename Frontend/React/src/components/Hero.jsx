import React from "react";
import Button from "./Button";
import GlassPlaceholder from "./GlassPlaceholder";
import firstLeaf from "/hero-leaves-1.png";
import secondLeaf from "/hero-leaves-2.png";
import thirdLeaf from "/hero-leaves-3.png";
import { ArrowDown } from "./SVG";

export default function Hero({ plantsCounter, scrollToCollection }) {
  const glassText = (
    <>
      <h3 className="hero__shopping__title">
        {Math.floor(plantsCounter / 10) * 10}+ Plants
      </h3>
      <p className="hero__shopping__text">
        We want our visitors to be inspire to get their hands dirty
      </p>
    </>
  );

  const glassImages = (
    <ul className="leaves__list">
      <li className="leaves__item">
        <img className="leaves__image" src={firstLeaf} />
      </li>
      <li className="leaves__item">
        <img className="leaves__image" src={secondLeaf} />
      </li>
      <li className="leaves__item">
        <img className="leaves__image" src={thirdLeaf} />
      </li>
    </ul>
  );

  return (
    <div className="hero">
      <div className="overlay"></div>
      <div className="hero__info">
        <h1 className="hero__title">growth</h1>
        <p className="hero__description">
          We're your online houseplant destination. We offer a wide range of
          houseplants and accessories shipped directly from our greenhouse to
          yours!
        </p>
      </div>
      <div className="hero__shopping">
        <div className="hero__shopping__description">
          <GlassPlaceholder content={glassText} radius={32} hasBorder={true} />
          <GlassPlaceholder
            content={glassImages}
            radius={32}
            hasBorder={true}
          />
        </div>
        <Button
          content={<ArrowDown />}
          btnRound={true}
          size={92}
          onClick={scrollToCollection}
        />
        <div className="hero__shopping__button">
          <Button
            content="Shop Tropical Plants"
            btnLarge={true}
            btnLight={true}
          />
        </div>
      </div>
    </div>
  );
}
