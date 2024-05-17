import { getPlant } from "../api/plants";

export const plantLoader = async ({ params }) => {
  return await getPlant(params.plantSlug);
}
