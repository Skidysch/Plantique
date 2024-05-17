import instance from "./axios";

export async function getPlants() {
  
  const { data } = await instance.get("/plants");
  return data;
}

export async function getPlant(plantSlug) {
  const { data } = await instance.get(`/plants/slug/${plantSlug}`)
  return data;
}

export async function filterPlantsByCategory(categoryId) {
  
  const { data } = await instance.get(`/plants/filter/${categoryId}`);
  return data;
}