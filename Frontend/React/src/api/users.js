export async function getCurrentUser() {
  const requestOptions = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("authToken")}`,
    },
  };
  const response = await fetch("/api/users/current", requestOptions);
  const data = response.json();
  return data;
}
