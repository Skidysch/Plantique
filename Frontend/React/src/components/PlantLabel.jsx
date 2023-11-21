import React from "react";
import PlantLabelIcon from '/plant-label-icon.svg';

export default function PlantLabel({title}) {
  return (
    <a href="#">
      <div className="plant-label">
        <div className="plant-label__icon">
          <img src={PlantLabelIcon} alt="Plant label icon" />
        </div>
        <div className="plant-label__title">
          {title}
        </div>
      </div>
    </a>
  )
}