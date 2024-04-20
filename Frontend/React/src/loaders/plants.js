import { getPlant } from "../api/plants";

export const plantLoader = async ({ params }) => {
  const plant = await getPlant(params.plantSlug);
  return plant;
}
