import React from "react";
import CategoryCard from "./CategoryCard";

export default function IndoorCollection({ title, categories, theme }) {
  return (
    <div className="collection__category">
      <div className="collection__header">
        <div className="collection__inner">
          <h2 className={'collection__title' + (theme === 'dark' ? ' collection__title--dark' : '')}>{title}</h2>
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
