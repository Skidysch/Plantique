export async function getPlants() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  
  const response = await fetch("/api/plants", requestOptions);
  const data = await response.json();
  return data;
}

export async function getPlant(plantSlug) {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await fetch(`/api/plants/${plantSlug}`, requestOptions)
  const data = await response.json();
  return data;
}

export async function filterPlantsByCategory(categoryId) {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch(`/api/plants/filter/${categoryId}`, requestOptions);
  const data = await response.json();
  return data;
}