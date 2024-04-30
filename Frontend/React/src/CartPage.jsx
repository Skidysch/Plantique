import { useState } from "react";
import { useLoaderData } from "react-router-dom";

import CartItem from "./components/CartItem";
import Button from "./components/Button";
import { TrashCan } from "./components/SVG";
import "./styles/CartPage.css";

const CartPage = () => {
  const cart = useLoaderData();
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
    const deletedItem = cartItems.filter(item => item.id === associationId)[0]

    setTotalItems((prevState) => prevState - deletedItem.quantity)
    setTotalPrice((prevState) => prevState - deletedItem.plant.price * deletedItem.quantity)
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
            <Button content="Order" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default CartPage;
