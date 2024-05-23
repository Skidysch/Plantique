import React, { useEffect, useState } from "react";
import Button from "./Button";
import FiltersList from "./FiltersList";
import FilterCategoryCard from "./FilterCategoryCard";
import { filterCategoriesByCollection } from "../api/categories";
import { Link } from "react-router-dom";

export default function FilterCollections({ collections }) {
  const [categories, setCategories] = useState([]);
  useEffect(() => {
    filterCategoriesByCollection(collections[0]?.id).then((result) =>
      setCategories(result)
    );
  }, []);

  return (
    <div className="collection__filters">
      <div className="collection__filters__header">
        <FiltersList collections={collections} setCategories={setCategories} />
        <Link to="/collections">
          <Button content="See All" btnLight={true} />
        </Link>
      </div>
      <ul className="collection__filters__categories__list">
        {categories.map((item, index) => (
          <FilterCategoryCard key={index} {...item} />
        ))}
      </ul>
    </div>
  );
}
