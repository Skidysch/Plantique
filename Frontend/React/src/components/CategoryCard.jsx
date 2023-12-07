import React, { useState } from "react";
import Button from "./Button";
import { ArrowRight } from "./SVG";

export default function CategoryCard(props) {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const hoverClass = isHovered ? "category-card--hovered " : "";

  const cardStyles = {
    backgroundImage: `url(${props.cover})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
  };

  const glassStyles = {
    background: "rgba(255, 255, 255, 0.10)",
    backdropFilter: "blur(12.5px)",
  };

  return (
    <div
      className={"category-card " + hoverClass}
      style={cardStyles}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <div className="category-card__button">
        <a href="#">
          <Button content={<ArrowRight />} btnRound={true} size={60} />
        </a>
      </div>
      <div
        className="category-card__info"
        style={
          isHovered
            ? glassStyles
            : { background: "transparent", backdropFilter: "none" }
        }
      >
        <a href="#">
          <h3 className="category-card__title">{props.title}</h3>
        </a>
        <p className="category-card__description">{props.description}</p>
      </div>
    </div>
  );
}
