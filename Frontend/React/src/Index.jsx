import React from "react";

import Hero from "./components/Hero";
import Purpose from "./components/Purpose";
import Collection from "./components/Collection";
import Offering from "./components/Offering";
import Questions from "./components/Questions";
import { useLoaderData } from "react-router-dom";

export default function Index() {
  const { collections, categories, plants } = useLoaderData();
  // categories = categories.slice(0, 4);

  return (
    <div>
      <Hero />
      <Purpose />
      <Collection
        collections={collections}
        categories={categories}
        plants={plants}
      />
      <Offering />
      <Questions />
    </div>
  );
}
