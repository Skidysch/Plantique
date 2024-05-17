import instance from "./axios";

export async function getCategories() {
  const { data } = await instance.get("/categories");
  return data;
}

export async function getCategory(categorySlug) {
  const { data } = await instance.get(`/categories/slug/${categorySlug}`)
  return data;
}

export async function filterCategoriesByCollection(collectionId) {
  const { data } = await instance.get(`/categories/filter/${collectionId}`);
  return data;
}