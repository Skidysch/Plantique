import React from "react";

import Hero from "./components/Hero";
import Purpose from "./components/Purpose";
import Collection from "./components/Collection";
import Offering from "./components/Offering";
import Questions from "./components/Questions";
import { useLoaderData } from "react-router-dom";

export default function Index() {
  const { collections, categories, plants } = useLoaderData();

  return (
    <div>
      <Hero plantsCounter={plants.length} />
      <Purpose />
      <Collection
        collections={collections}
        categories={categories.filter(c => c.collection_id === collections[0].id)}
        plants={plants}
      />
      <Offering />
      <Questions />
    </div>
  );
}
