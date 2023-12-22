export async function getPlants() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch("/api/plants", requestOptions);
  const data = response.json();
  return data;
}
