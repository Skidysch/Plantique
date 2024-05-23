import { useContext, useState } from "react";
import { Form, Link, useLoaderData, useActionData } from "react-router-dom";
import Button from "./components/Button";

import "./styles/PlantPage.css";
import { UserContext } from "./context/UserContext";
import instance from "./api/axios";

const submitForm = async (data) => {
  const requestData = JSON.stringify({ quantity: data.quantity });

  const response = await instance.post(
    `/carts/id/${data.userId}/add/${data.plantId}`,
    requestData
  );

  if (response.statusText !== "OK") {
    return { errorMessage: response.data.detail };
  } else {
    return {
      successMessage: "Plant successfully added to cart",
    };
  }
};

export const addToPlantAction = async ({ request }) => {
  const formData = await request.formData();
  const data = Object.fromEntries(formData);

  return await submitForm(data);
};

export default function PlantPage() {
  const plant = useLoaderData();
  const data = useActionData();
  const { user } = useContext(UserContext);
  const [quantity, setQuantity] = useState(1);

  const styles = {
    backgroundImage: `url(${plant?.image_url})`,
  };

  const handleChangeQuantity = (value) => {
    value =
      parseInt(value) <= 0
        ? 1
        : parseInt(value) >= plant.stock_quantity
        ? plant.stock_quantity
        : value;
    setQuantity(value);
  };

  return (
    <section className="plant" style={styles}>
      <div className="glass-bg"></div>
      <div className="plant__content">
        <div className="plant__left">
          <div className="plant__image">
            <img src={plant?.image_url} alt="Plant image" />
          </div>
        </div>
        <div className="plant__right">
          <h1 className="plant__title">{plant?.name}</h1>
          <p className="plant__price">Price: ${plant?.price}</p>
          <p className="plant__stock">In stock: {plant?.stock_quantity} pcs.</p>
          <Form
            className="form form--invisible"
            method="post"
            action={plant?.link}
          >
            <div className="form__buttons">
              <label htmlFor="quantity">
                <input
                  className="form__input"
                  type="number"
                  name="quantity"
                  id="quantity"
                  value={quantity}
                  onChange={(e) => handleChangeQuantity(e.target.value)}
                  placeholder="Quantity"
                />
              </label>
              <label htmlFor="userId">
                <input
                  className="form__input"
                  type="hidden"
                  name="userId"
                  id="userId"
                  value={user?.id}
                />
              </label>
              <label htmlFor="plantId">
                <input
                  className="form__input"
                  type="hidden"
                  name="plantId"
                  id="plantId"
                  value={plant?.id}
                />
              </label>
              <Button content="Add to cart" btnDark={true} />
            </div>
          </Form>
          <p className="plant__soil-type">Soil: {plant?.soil_type}</p>
          <p className="plant__categories">
            Categories:{" "}
            {plant?.categories.map((category) => (
              <Link
                className="plant__categories__link"
                key={category.id}
                to={category.link}
              >
                {category.name}
              </Link>
            ))}
          </p>
          <p className="plant__description">{plant?.description}</p>
        </div>
      </div>
      {data?.successMessage && (
        <div className="notification-popup">
          <p className="form__success">{data.successMessage}</p>
        </div>
      )}
      {data?.errorMessage && (
        <div className="notification-popup">
          <p className="form__error">{data.errorMessage}</p>
        </div>
      )}
    </section>
  );
}
