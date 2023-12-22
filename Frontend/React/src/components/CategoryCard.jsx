import React, { useState } from "react";
import Button from "./Button";
import { ArrowRight } from "./SVG";
import { Link } from "react-router-dom";

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
    backgroundImage: `url(${props.image_url})`,
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
        <Link to={props.link}>
          <Button content={<ArrowRight />} btnRound={true} size={60} />
        </Link>
      </div>
      <div
        className="category-card__info"
        style={
          isHovered
            ? glassStyles
            : { background: "transparent", backdropFilter: "none" }
        }
      >
        <Link to={props.link}>
          <h3 className="category-card__title">{props.name}</h3>
        </Link>
        <p className="category-card__description">{props.description}</p>
      </div>
    </div>
  );
}
