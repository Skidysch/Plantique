import React, { useRef } from "react";

import Hero from "./components/Hero";
import Purpose from "./components/Purpose";
import Collection from "./components/Collection";
import Offering from "./components/Offering";
import Questions from "./components/Questions";
import { useLoaderData } from "react-router-dom";

export default function Index() {
  const { collections, categories, plants } = useLoaderData();

  const targetRef = useRef(null);

  const scrollToElement = () => {
    const headerHeight = document.getElementById('header').offsetHeight;

    if (targetRef.current) {
      window.scrollTo({
        top: targetRef.current.offsetTop - headerHeight - 20,
        behavior: "smooth",
      });
    }
  };

  return (
    <div>
      <Hero
        plantsCounter={plants?.length}
        scrollToCollection={scrollToElement}
      />
      <Purpose />
      <Collection
        targetRef={targetRef}
        collections={collections}
        categories={categories.filter(
          (c) => c.collection_id === collections[0].id
        )}
        plants={plants}
      />
      <Offering />
      <Questions />
    </div>
  );
}
