import React from "react";
import FilteringCollection from "./FilteringCollection";
import NewCollection from "./NewCollection";
import CategoryCollection from "./CategoryCollection";


export default function Collection() {
  return (
    <div className="collection">
      <FilteringCollection />
      <NewCollection />
      <CategoryCollection />
    </div>
  )
}