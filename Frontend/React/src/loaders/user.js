import { getCurrentUser } from "../api/users";

export async function loaderCurrentUser() {
  const user = await getCurrentUser();
  return { user };
}