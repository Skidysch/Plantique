import { getCart } from "../api/carts";

export const cartLoader = async ({ params }) => {
  const cart = await getCart(params.userId);
  return cart;
}
