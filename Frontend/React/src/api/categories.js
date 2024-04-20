export async function getCategories() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch("/api/v1/categories", requestOptions);
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

  const response = await fetch(`/api/v1/categories/slug/${categorySlug}`, requestOptions)
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
  const response = await fetch(`/api/v1/categories/filter/${collectionId}`, requestOptions);
  const data = await response.json();
  return data;
}