import React from "react";
import Button from "./Button";
import FiltersList from "./FiltersList";
import FilterCard from "./FilterCard";

export default function FilteringCollection() {
  const filterCards = [
    {'title': "Pet Friendly Plants",
    'description': "Discover pet-safe plants that add natural beauty to your home while ensuring the well-being of your furry friends.",
    'cover': '/filter-card-1.png'},
    {'title': "Orchids",
    'description': "Orchids are easily everyones Favorite flowering plant, Find new orchids and orchids success items in this collection",
    'cover': '/filter-card-2.png'},
    {'title': "Succulents",
    'description': "All Succulents are cacti, but not all cacti are succulents. Both make low maintence house pants.",
    'cover': '/filter-card-3.png'},
    {'title': "Succulents",
    'description': "All Succulents are cacti, but not all cacti are succulents. Both make low maintence house pants.",
    'cover': '/filter-card-3.png'}
  ]

  return (
    <div className="collection__filtering">
      <div className="collection__filters">
        <FiltersList />
        <Button content="See All"
                btnLight={true}
                 />
      </div>
      <ul className="filter__list">
        {filterCards.map((item, index) => <FilterCard key={index}
                                                       {...item} />)}
      </ul>
    </div>
  )
}