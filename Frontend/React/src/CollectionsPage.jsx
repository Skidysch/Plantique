import { useLoaderData } from "react-router-dom";
import IndoorCollection from "./components/IndoorCollection";

import "./styles/CollectionsPage.css";

const CollectionsPage = () => {
  const { collections, categories} = useLoaderData();

  const styles = {
    backgroundImage: `url('/collections-bg.jpg')`,
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
