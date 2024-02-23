import { getCategory } from "../api/categories";
import { filterPlantsByCategory } from "../api/plants";

export const categoryLoader = async ({ params }) => {
  const category = await getCategory(params.categorySlug);
  console.log(category?.id)
  const plants = await filterPlantsByCategory(category?.id);
  return { category, plants };
}