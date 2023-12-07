import React from "react";
import Button from "./Button";

export default function FiltersList() {
  const buttonsList = [
    "Outdoor Plant",
    "Indoor Plant",
    "Flower Pot",
    "Potted Plant",
  ];

  return (
    <ul className="collection__filters__list">
      {buttonsList.map((item, index) => (
        <Button key={index} content={item} btnLight={true} />
      ))}
    </ul>
  );
}
