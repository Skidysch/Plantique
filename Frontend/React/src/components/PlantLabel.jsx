import React from "react";
import {PlantLabelIcon} from './SVG';

export default function PlantLabel({title}) {
  return (
    <a href="#">
      <div className="plant-label">
        <div className="plant-label__icon">
          <PlantLabelIcon />
        </div>
        <div className="plant-label__title">
          {title}
        </div>
      </div>
    </a>
  )
}