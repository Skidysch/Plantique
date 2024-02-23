import React from "react";

import "./styles/CollectionsPage.css";
import { useLoaderData } from "react-router-dom";
import IndoorCollection from "./components/IndoorCollection";

const CollectionsPage = () => {
  const { collections, categories} = useLoaderData();

  const styles = {
    backgroundImage: `url('/hero-bg.jpeg')`,
  };

  return (
    <section className="collections" style={styles}>
      <div className="glass-bg"></div>
      <div className="collections__content">
        {collections.map((collection) => {
          const categories_filtered = categories.filter(cat => cat.collection_id === collection.id)
          return (
            <div className="collections__collection" key={collection.slug}>
              <IndoorCollection title={collection.name} categories={categories_filtered} theme='dark' />
            </div>
          );
        })}
      </div>
    </section>
  );
};

export default CollectionsPage;
