import React from "react";
import SwiperPlants from "./swiper/SwiperPlants";

export default function NewCollection() {
  return (
    <div className="collection__new">
      <div className="collection__header">
        <div className="collection__inner">
          <h2 className="collection__title">New Plants</h2>
          <p className="collection__description">
            Bring nature insider and shop our big selections of fresh indoor
            plants including Instagram-worthy houseplants, pet-friendly plants,
            orchids and one-of-a-kind rare plants.
          </p>
        </div>
      </div>
      <SwiperPlants />
    </div>
  );
}
