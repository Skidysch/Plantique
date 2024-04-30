export async function getCart(userId) {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await fetch(`/api/v1/carts/id/${userId}`, requestOptions)
  const data = await response.json();
  return data;
}