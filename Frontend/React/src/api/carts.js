import instance from "./axios";

export async function getCart(userId) {
  const { data } = await instance.get(`/carts/id/${userId}`);
  return data;
}
