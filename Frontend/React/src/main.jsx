import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import App from "./App";
import Index from "./Index";
import Login, { action as loginAction } from "./Login";
import Register, { action as registerAction } from "./Register";
import ErrorPage from "./ErrorPage";
import { UserProvider } from "./context/UserContext";

import "./styles/index.css";
import Profile, { loaderCurrentUser } from "./Profile";
import ProfileDelete, { profileDeleteAction } from "./components/ProfileDelete";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        index: true,
        element: <Index />,
      },
      {
        path: "/login",
        element: <Login />,
        action: loginAction,
      },
      {
        path: "/register",
        element: <Register />,
        action: registerAction,
      },
      {
        path: "/profile",
        element: <Profile />,
        loader: loaderCurrentUser,
        children: [
          {
            path: "/profile/delete/:userId",
            element: <ProfileDelete />,
            action: profileDeleteAction,
          }
        ],
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <UserProvider>
      <RouterProvider router={router} />
    </UserProvider>
  </React.StrictMode>
);
