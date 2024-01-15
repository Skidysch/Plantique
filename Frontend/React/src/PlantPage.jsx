import React from "react";
import { Form, useLoaderData } from "react-router-dom";
import { getPlant } from "./api/plants";
import Button from "./components/Button";

import "./styles/PlantPage.css";

export async function plantLoader({ params }) {
  const plant = await getPlant(params.plantSlug);
  return { plant };
}

export default function PlantPage() {
  const { plant } = useLoaderData();
  console.log(plant);

  const styles = {
    backgroundImage: `url(${plant.image_url})`,
  };

  return (
    <section className="plant" style={styles}>
      <div className="glass-bg"></div>
      <div className="plant__content">
        <div className="plant__left">
          <div className="plant__image">
            <img src={plant.image_url} alt="Plant image" />
          </div>
        </div>
        <div className="plant__right">
          <h1 className="plant__title">{plant.name}</h1>
          <p className="plant__price">$ {plant.price}</p>
          <Form
            className="form form--invisible"
            method="post"
            action={plant.link}
          >
            <div className="form__buttons">
              <label htmlFor="quantity">
                <input
                  className="form__input"
                  type="number"
                  name="quantity"
                  id="quantity"
                  placeholder="Quantity"
                />
              </label>
              <Button content="Add to cart" btnDark={true} />
            </div>
          </Form>
          <p className="plant__soil-type">Soil: {plant.soil_type}</p>
          <p className="plant__categories">
            Categories:{" "}
            {plant.categories.map((item, index) => {
              return `${item.name} `;
            })}
          </p>
          <p className="plant__description">{plant.description}</p>
        </div>
      </div>
    </section>
  );
}
