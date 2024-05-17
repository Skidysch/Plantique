import instance from "./axios";

export async function getCollections() {
  const { data } = await instance.get("/collections");
  return await data;
}
