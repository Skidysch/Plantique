import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Pagination } from "swiper/modules";
import PlantCard from "../PlantCard";

import "swiper/css";
import "swiper/css/pagination";

export default function SwiperPlants() {
  return (
    <Swiper
      className="plants__slider"
      modules={[Pagination]}
      spaceBetween={10}
      slidesPerView={1}
      onSlideChange={() => console.log("slide change")}
      onSwiper={(swiper) => console.log(swiper)}
      pagination={{ clickable: true, dynamicBullets: true }}
      rewind={true}
      breakpoints={{
        600: {
          slidesPerView: 2,
        },
        998: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
      }}
    >
      <SwiperSlide>
        <PlantCard
          title="Peperomia Plants"
          cover="/plant-card-1.png"
          soil="Moist but well-drained"
          price="₹122,056"
        />
      </SwiperSlide>
      <SwiperSlide>
        <PlantCard
          title="Fiddle-Leaf Fig"
          cover="/plant-card-2.png"
          soil="Moist but well-drained"
          price="₹162,056"
        />
      </SwiperSlide>
      <SwiperSlide>
        <PlantCard
          title="Calathea Orbifolia"
          cover="/plant-card-3.png"
          soil="Moist but well-drained"
          price="₹102,056"
        />
      </SwiperSlide>
      <SwiperSlide>
        <PlantCard
          title="Fiddle-Leaf Fig"
          cover="/plant-card-2.png"
          soil="Moist but well-drained"
          price="₹162,056"
        />
      </SwiperSlide>
      <SwiperSlide>
        <PlantCard
          title="Calathea Orbifolia"
          cover="/plant-card-3.png"
          soil="Moist but well-drained"
          price="₹102,056"
        />
      </SwiperSlide>
    </Swiper>
  );
}
