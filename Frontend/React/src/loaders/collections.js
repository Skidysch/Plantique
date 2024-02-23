import { getCategories } from "../api/categories";
import { getCollections } from "../api/collections";

export const collectionsLoader = async () => {
  const collections = await getCollections();
  const categories = await getCategories();
  return { collections, categories };
}