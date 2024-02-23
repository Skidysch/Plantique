export async function getCurrentUser(
  token = localStorage.getItem("authToken")
) {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  };
  const response = await fetch("/api/users/current", requestOptions);
  const data = await response.json();
  return data;
}
