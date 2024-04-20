import React, { createContext, useEffect, useState } from "react";

export const UserContext = createContext();

export const UserProvider = (props) => {
  const [token, setToken] = useState(localStorage.getItem("authToken"));
  const [user, setUser] = useState(localStorage.getItem("authUser"));

  useEffect(() => {
    const fetchUser = async () => {
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      };

      const response = await fetch("/api/v1/jwt/users/current", requestOptions);

      if (!response.ok) {
        setToken(null);
        setUser(null);
      }
      localStorage.setItem("authToken", token);
      localStorage.setItem("authUser", user);
    };
    // await?
    fetchUser();
  }, [token, user]);

  return (
    <UserContext.Provider value={{token, setToken, user, setUser}}>
      {props.children}
    </UserContext.Provider>
  );
};
