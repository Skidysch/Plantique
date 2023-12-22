import React from "react";
import Button from "./Button";

export default function FiltersList({ collections }) {

  return (
    <ul className="collection__filters__list">
      {collections.map((item, index) => (
        <Button key={index} content={item.name} btnLight={true} />
      ))}
    </ul>
  );
}
