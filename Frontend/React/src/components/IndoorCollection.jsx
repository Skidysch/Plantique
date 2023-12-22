import React from "react";
import CategoryCard from "./CategoryCard";

export default function IndoorCollection({ categories }) {
  categories = categories.slice(0, 4);

  return (
    <div className="collection__category">
      <div className="collection__header">
        <div className="collection__inner">
          <h2 className="collection__title">Indoor Collection</h2>
        </div>
      </div>
      <ul className="category__list">
        {categories.map((item, index) => {
          return (
            <CategoryCard
              key={index}
              {...item}
            />
          );
        })}
      </ul>
    </div>
  );
}
