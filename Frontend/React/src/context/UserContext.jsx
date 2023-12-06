import React, { createContext, useEffect, useState } from 'react';

export const UserContext = createContext();

export const UserProvider = (props) => {
  const [token, setToken] = useState(localStorage.getItem('authToken'))

  useEffect(() => {
    const fetchUser = async () => {
      const requestOptions = {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
      };

      const response = await fetch('/api/users/current/', requestOptions)

      if (!response.ok) {
        setToken(null);
      }
      localStorage.setItem('authToken', token);
    };
    // await?
    fetchUser();
  }, [token]);

  return (
    <UserContext.Provider value={[token, setToken]}>
      {props.children}
    </UserContext.Provider>
  )
}