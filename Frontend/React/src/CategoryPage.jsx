import React from "react";
import { useLoaderData } from "react-router-dom";

import "./styles/categoryPage.css";
import PlantCard from "./components/PlantCard";

export default function CategoryPage() {
  const { category, plants }= useLoaderData();

  const styles = {
    backgroundImage: `url(${category.image_url})`,
  };

  return (
    <section className="category" style={styles}>
      <div className="glass-bg"></div>
      <div className="category__content">
          <h1 className="category__title">{category.name}</h1>
          <p className="category__description">{category.description}</p>
          <ul className="category__plants">
          {plants.map((plant) => (
            <li className="category__plant" key={plant.slug}>
              <PlantCard {...plant}/>
            </li>
          ))}
          </ul>
      </div>
    </section>
  );
}
