import React, { useState } from "react";
import PlantLabel from "./PlantLabel";

export default function FilterCard(props) {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  }

  const handleMouseLeave = () => {
    setIsHovered(false);
  }

  const hoverClass = isHovered ? 'filter-card--hovered ' : '';
  
  const styles = {
    backgroundImage: `url(${props.cover})`,
  }

  return (
    <div className={"filter-card " + hoverClass}
         style={styles}
         onMouseEnter={handleMouseEnter}
         onMouseLeave={handleMouseLeave}
    >
      <div className="filter-card__info">
        <a href="#">
          <h4 className="filter-card__title">
            {props.title}
          </h4>
        </a>
        <p className="filter-card__description">
          {props.description}
        </p>
      </div>
      <div className="filter-card__goods">
        <PlantLabel title="Piperaceae"/>
        <PlantLabel title="Araceae"/>
      </div>
    </div>
  )
}