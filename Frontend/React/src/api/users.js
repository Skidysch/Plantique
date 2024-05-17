import instance from "./axios";


export async function getCurrentUser(
  token,
) {
  const requestOptions = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
  try {
    const response = await instance.get("/jwt/users/current", requestOptions);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}
