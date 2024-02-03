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

export async function getPlant(identifier) {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await fetch(`/api/plants/${identifier}`, requestOptions)
  const data = response.json();
  return data;
}