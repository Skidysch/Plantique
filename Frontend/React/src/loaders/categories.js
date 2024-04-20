import { getCategory } from "../api/categories";
import { filterPlantsByCategory } from "../api/plants";

export const categoryLoader = async ({ params }) => {
  const category = await getCategory(params.categorySlug);
  // Can't I just extract needed data from the category?
  const plants = await filterPlantsByCategory(category?.id);
  return { category, plants };
}