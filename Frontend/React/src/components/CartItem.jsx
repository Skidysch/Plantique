import { useState } from "react";
import Button from "./Button";
import { Form, Link } from "react-router-dom";
import instance from "../api/axios";

const CartItem = ({ value, item, setTotalItems, setTotalPrice }) => {
  const [quantity, setQuantity] = useState(value);

  const handleChangeQuantity = async (associationId, value, replace) => {
    if (replace) {
      value =
        parseInt(value) <= 0
          ? 1
          : parseInt(value) >= item.plant.stock_quantity
          ? item.plant.stock_quantity
          : value;
      setTotalItems(
        (prevState) => parseInt(prevState) + parseInt(value - quantity)
      );
      setTotalPrice(
        (prevState) => prevState + item.plant.price * (value - quantity)
      );
      setQuantity(value);
    } else {
      setQuantity((prevState) => prevState + value);
      setTotalItems((prevState) => prevState + value);
      setTotalPrice((prevState) => prevState + item.plant.price * value);
    }

    const requestData = JSON.stringify({ quantity: value, replace: replace });

    await instance.patch(`/carts/update/${associationId}`, requestData);
  };

  return (
    <>
      <Link to={item.plant.link} className="cart__items__item__image">
        <img src={item.plant.image_url} alt={item.plant.name} />
      </Link>
      <div className="cart__items__item__details">
        <Link to={item.plant.link} className="cart__items__item__link">
          <h2 className="cart__items__item__name">{item.plant.name}</h2>
        </Link>
        <Form className="form form--invisible">
          <div className="form__buttons">
            <Button
              disabled={quantity <= 1}
              onClick={() => handleChangeQuantity(item.id, -1, false)}
              size={60}
              content="-"
              btnDark={true}
              btnRound={true}
            />
            <label htmlFor="quantity">
              <input
                className="form__input form__input--cart"
                type="number"
                name="quantity"
                id="quantity"
                value={quantity}
                onChange={(e) =>
                  handleChangeQuantity(item.id, e.target.value, true)
                }
              />
            </label>
            <Button
              onClick={() => handleChangeQuantity(item.id, 1, false)}
              size={60}
              content="+"
              btnDark={true}
              btnRound={true}
              disabled={quantity >= item.plant.stock_quantity}
            />
          </div>
        </Form>
        <div className="cart__items__item__price__footer">
          <span className="cart__items__item__price">
            Total: ${item.plant.price * quantity}
          </span>
        </div>
      </div>
    </>
  );
};

export default CartItem;
