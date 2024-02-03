import { getPlants, getPlant } from "../api/plants";
import { getCollections } from "../api/collections";
import { getCategories } from "../api/categories";

export const plantsLoader = async () => {
  const collections = await getCollections();
  const categories = await getCategories();
  const plants = await getPlants();

  return { collections, categories, plants };
}

export const plantLoader = async ({ params }) => {
  const plant = await getPlant(params.plantSlug);
  return plant;
}