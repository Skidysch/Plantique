import { getPlants } from "../api/plants";
import { getCollections } from "../api/collections";
import { getCategories } from "../api/categories";

export const rootLoader = async () => {
  const collections = await getCollections();
  const categories = await getCategories();
  const plants = await getPlants();

  return { collections, categories, plants };
}