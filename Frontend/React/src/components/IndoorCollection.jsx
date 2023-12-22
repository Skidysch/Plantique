import React from "react";
import CategoryCard from "./CategoryCard";

export default function IndoorCollection() {
  return (
    <div className="collection__category">
      <div className="collection__header">
        <div className="collection__inner">
          <h2 className="collection__title">Indoor Collection</h2>
        </div>
      </div>
      <ul className="category__list">
        <CategoryCard
          cover="/category-card-1.png"
          title="Philodendron"
          description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed congue interdum ligula a dignissim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis orci elementum egestas lobortis."
        />
        <CategoryCard
          cover="/category-card-2.png"
          title="Calathea"
          description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed congue interdum ligula a dignissim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis orci elementum egestas lobortis."
        />
        <CategoryCard
          cover="/category-card-3.png"
          title="Air Purifying"
          description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed congue interdum ligula a dignissim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis orci elementum egestas lobortis."
        />
        <CategoryCard
          cover="/category-card-4.png"
          title="Low Light Tolerant"
          description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed congue interdum ligula a dignissim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis orci elementum egestas lobortis."
        />
      </ul>
    </div>
  );
}
