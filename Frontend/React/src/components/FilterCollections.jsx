import React from "react";
import Button from "./Button";
import FiltersList from "./FiltersList";
import FilterCategoryCard from "./FilterCategoryCard";

export default function FilterCollections({ collections, categories }) {
  return (
    <div className="collection__filters">
      <div className="collection__filters__header">
        <FiltersList collections={collections} />
        <Button content="See All" btnLight={true} />
      </div>
      <ul className="collection__filters__categories__list">
        {categories.map((item, index) => (
          <FilterCategoryCard key={index} {...item} />
        ))}
      </ul>
    </div>
  );
}
