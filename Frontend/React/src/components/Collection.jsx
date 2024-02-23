import React from "react";
import FilterCollections from "./FilterCollections";
import NewPlants from "./NewPlants";
import IndoorCollection from "./IndoorCollection";

export default function Collection({ collections, categories, plants }) {
  return (
    <div className="collection">
      <FilterCollections collections={collections} />
      <NewPlants plants={plants} />
      <IndoorCollection categories={categories} title='Indoor Collection'/>
    </div>
  );
}
