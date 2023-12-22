import React from "react";
import { PlantLabelIcon } from "./SVG";
import { Link } from "react-router-dom";

export default function PlantLabel({ title, link }) {
  return (
    <Link to={link}>
      <div className="plant-label">
        <div className="plant-label__icon">
          <PlantLabelIcon />
        </div>
        <div className="plant-label__title">{title}</div>
      </div>
    </Link>
  );
}
