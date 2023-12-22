export async function getCategories() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch("/api/categories", requestOptions);
  const data = response.json();
  return data;
}
