import React, { createContext, useEffect, useState } from "react";

export const UserContext = createContext();

export const UserProvider = (props) => {
  const [token, setToken] = useState(localStorage.getItem("authToken"));
  const [user, setUser] = useState(JSON.parse(localStorage.getItem("authUser")));

  useEffect(() => {
    const fetchUser = async (inputToken) => {
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${inputToken}`,
        },
      };

      const response = await fetch("/api/v1/jwt/users/current", requestOptions);
      if (!response.ok) {
        setUser(null);
        localStorage.setItem("authUser", null);
      } else {
        const user_obj = await response.json();
        setUser(user_obj);
        localStorage.setItem("authUser", JSON.stringify(user_obj));
      }
    };
    // await?
    fetchUser(token);
  }, [token]);

  return (
    <UserContext.Provider value={{ token, setToken, user, setUser }}>
      {props.children}
    </UserContext.Provider>
  );
};
