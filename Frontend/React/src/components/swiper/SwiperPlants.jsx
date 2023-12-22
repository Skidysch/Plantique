import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Pagination } from "swiper/modules";
import PlantCard from "../PlantCard";

import "swiper/css";
import "swiper/css/pagination";

export default function SwiperPlants({ plants }) {
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
      {plants.map((item, index) => (
        <SwiperSlide key={index}>
          <PlantCard {...item} />
        </SwiperSlide>
      ))}
    </Swiper>
  );
}
