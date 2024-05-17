import { createContext, useEffect, useState } from "react";
import { getCurrentUser } from "../api/users";

export const UserContext = createContext();

export const UserProvider = (props) => {
  const [token, setToken] = useState(localStorage.getItem("authToken"));
  const [user, setUser] = useState();

  useEffect(() => {
    const fetchUser = async (inputToken) => {
      
      if (token === null) {
        setUser(null);
      } else {
        const response = await getCurrentUser(inputToken);
        setUser(response);
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
