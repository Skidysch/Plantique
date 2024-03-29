export async function getCollections() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const response = await fetch("/api/collections", requestOptions);
  const data = await response.json();
  return await data;
}
