import { getCart } from "../api/carts";

export const cartLoader = async ({ params }) => {
  return await getCart(params.userId);
}
