import React, { useState } from "react";
import PlantLabel from "./PlantLabel";
import { Link } from "react-router-dom";

export default function FilterCard(props) {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const hoverClass = isHovered ? "filter-category-card--hovered " : "";

  const styles = {
    backgroundImage: `url(${props.image_url})`,
  };

  const glassStyles = {
    background: "rgba(255, 255, 255, 0.10)",
    backdropFilter: "blur(12.5px)",
  };

  return (
    <li
      className={"filter-category-card " + hoverClass}
      style={styles}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <div className="filter-category-card__info" style={isHovered ? glassStyles : { background: "transparent", backdropFilter: "none" }}>
        <Link to={props.link}>
          <h4 className="filter-category-card__title">{props.name}</h4>
        </Link>
        <p className="filter-category-card__description">{props.description}</p>
      </div>
      <div className="filter-category-card__goods">
        <PlantLabel title={props.plants[0].name} link={props.plants[0].link} />
        <PlantLabel title={props.plants[1].name} link={props.plants[1].link} />
      </div>
    </li>
  );
}
