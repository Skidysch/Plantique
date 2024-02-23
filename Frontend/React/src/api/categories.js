export async function getCategories() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch("/api/categories", requestOptions);
  const data = await response.json();
  return data;
}

export async function getCategory(categorySlug) {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await fetch(`/api/categories/${categorySlug}`, requestOptions)
  const data = await response.json();
  return data;
}

export async function filterCategoriesByCollection(collectionId) {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch(`/api/categories/filter/${collectionId}`, requestOptions);
  const data = await response.json();
  return data;
}