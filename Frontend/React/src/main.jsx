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
import Profile from "./Profile";
import ProfileDelete, { profileDeleteAction } from "./components/ProfileDelete";
import ProfileEdit, { profileEditAction } from "./components/ProfileEdit";
import PlantPage from "./PlantPage";
import CategoryPage from "./CategoryPage";
import { rootLoader } from "./loaders/root";
import { plantLoader } from "./loaders/plants";
import { categoryLoader } from "./loaders/categories";
import { loaderCurrentUser } from "./loaders/user";
import { collectionsLoader } from "./loaders/collections";
import CollectionsPage from "./CollectionsPage";

// TODO: learn to manage state with Redux, so I'll be able to optimise forms with redirect on actions.

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        index: true,
        element: <Index />,
        loader: rootLoader,
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
          },
          {
            path: "/profile/edit/:userId",
            element: <ProfileEdit />,
            action: profileEditAction,
          },
        ],
      },
      {
        path: "/categories/:categorySlug",
        element: <CategoryPage />,
        loader: categoryLoader,
      },
      {
        path: "/plants/:plantSlug",
        element: <PlantPage />,
        loader: plantLoader,
      },
      {
        path: '/collections',
        element: <CollectionsPage />,
        loader: collectionsLoader,
      }
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
