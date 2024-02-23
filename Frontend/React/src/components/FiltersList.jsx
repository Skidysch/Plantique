import React from "react";
import Button from "./Button";
import { filterCategoriesByCollection } from "../api/categories";

export default function FiltersList({ collections, setCategories }) {
  return (
    <select
      className="dropdown"
      onChange={(e) => {
        filterCategoriesByCollection(e.target.value).then((result) => {
          setCategories(result);
        });
      }}
    >
      {collections.map((collection) => (
        <option key={collection.slug} value={collection.id} className="dropdown__option">
          {collection.name}
        </option>
      ))}
    </select>
  );
}
