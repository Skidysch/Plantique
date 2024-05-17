import { useState } from "react";
import { Form, useActionData, useLoaderData } from "react-router-dom";
import instance from "./api/axios";
import { loadStripe } from "@stripe/stripe-js";

import CartItem from "./components/CartItem";
import Button from "./components/Button";
import { TrashCan } from "./components/SVG";
import "./styles/CartPage.css";

const stripePromise = loadStripe(import.meta.env.VITE_STRIPE_PUBLISH);

const submitCreateOrder = async (data) => {
  const requestOptions = { cart: JSON.parse(data.cart) };

  const response = await instance.post("/orders/create", requestOptions);
  if (response.status === 201) {
    try {
      const stripeResponse = await instance.post(
        `/payment/process/${response.data.order_id}`
      );
      const { stripe_session_id } = stripeResponse.data;

      // Redirect to Stripe
      const stripe = await stripePromise;
      await stripe.redirectToCheckout({ sessionId: stripe_session_id });
      return null;

    } catch (error) {
      console.log("Error creating checkout session: ", error);
    }
  } else {
    return { errorMessage: "Error occured while creating your order" };
  }
};

export const createOrderAction = async ({ request }) => {
  const formData = await request.formData();
  const orderData = Object.fromEntries(formData);

  return await submitCreateOrder(orderData);
};

const CartPage = () => {
  const cart = useLoaderData();
  const data = useActionData();
  const [cartItems, setCartItems] = useState(cart.plants_details);
  const [totalItems, setTotalItems] = useState(
    cart.plants_details.reduce((acc, item) => acc + item.quantity, 0)
  );
  const [totalPrice, setTotalPrice] = useState(
    cart.plants_details.reduce(
      (acc, item) => acc + item.plant.price * item.quantity,
      0
    )
  );

  const handleDeleteItem = async (associationId) => {
    const deletedItem = cartItems.filter(
      (item) => item.id === associationId
    )[0];

    setTotalItems((prevState) => prevState - deletedItem.quantity);
    setTotalPrice(
      (prevState) => prevState - deletedItem.plant.price * deletedItem.quantity
    );
    setCartItems((prevState) =>
      prevState.filter((item) => item.id !== associationId)
    );
    const requestOptions = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    };

    await fetch(`/api/v1/carts/delete/${associationId}`, requestOptions);
  };

  return (
    <div className="cart">
      <div className="glass-bg"></div>
      <div className="cart__inner">
        <div className="cart__inner__header">
          <h1 className="cart__inner__header__name">Your cart</h1>
        </div>
        <div className="cart__inner__body">
          <ul className="cart__items">
            {cartItems.map((item) => (
              <li key={item.id} className="cart__items__item">
                <CartItem
                  setTotalItems={setTotalItems}
                  setTotalPrice={setTotalPrice}
                  value={item.quantity}
                  item={item}
                />
                <div className="cart__items__item__delete">
                  <Button
                    onClick={() => handleDeleteItem(item.id)}
                    content={<TrashCan />}
                    size={60}
                    btnRound={true}
                  />
                </div>
              </li>
            ))}
          </ul>
          <div className="cart__inner__body__result">
            <h3 className="cart__inner__body__result__total-items">
              Total items: {totalItems}
            </h3>
            <p className="cart__inner__body__result__total-price">
              Total price: ${totalPrice}
            </p>
            <Form action={`/cart/${cart?.user_id}`} method="post">
              <label htmlFor="cart">
                <input
                  className="form__input"
                  type="hidden"
                  name="cart"
                  id="cart"
                  value={JSON.stringify(cart)}
                />
              </label>
              <Button content="Order" />
            </Form>
            {data?.errorMessage && (
              <p className="form__error">{data.errorMessage}</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default CartPage;
