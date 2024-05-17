import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

import App from "./App";
import { UserProvider } from "./context/UserContext";
import ErrorPage from "./ErrorPage";
import Index from "./Index";
import Login, { action as loginAction } from "./Login";
import Register, { action as registerAction } from "./Register";

import CategoryPage from "./CategoryPage";
import CollectionsPage from "./CollectionsPage";
import PlantPage, { addToPlantAction } from "./PlantPage";
import CartPage, { createOrderAction } from "./CartPage";
import ProfilePage from "./ProfilePage";
import ProfileDelete, { profileDeleteAction } from "./components/ProfileDelete";
import ProfileEdit, { profileEditAction } from "./components/ProfileEdit";
import ProfileEditPassword, {
  profileEditPasswordAction,
} from "./components/ProfileEditPassword";
import { rootLoader } from "./loaders/root";
import { categoryLoader } from "./loaders/categories";
import { collectionsLoader } from "./loaders/collections";
import { plantLoader } from "./loaders/plants";
import { cartLoader } from "./loaders/carts";
import "./styles/index.css";
import PaymentResultPage from "./PaymentResultPage";
import PaymentSuccess from "./components/PaymentSuccess";
import PaymentCancel from "./components/PaymentCancel";

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
        element: <ProfilePage />,
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
          {
            path: "/profile/edit/password/:userId",
            element: <ProfileEditPassword />,
            action: profileEditPasswordAction,
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
        action: addToPlantAction,
      },
      {
        path: "/collections",
        element: <CollectionsPage />,
        loader: collectionsLoader,
      },
      {
        path: "/cart/:userId",
        element: <CartPage />,
        loader: cartLoader,
        action: createOrderAction,
      },
      {
        path: "/payment",
        element: <PaymentResultPage />,
        children: [
          {
            path: "/payment/success",
            element: <PaymentSuccess />,
          },
          {
            path: "/payment/cancel",
            element: <PaymentCancel />,
          },
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
