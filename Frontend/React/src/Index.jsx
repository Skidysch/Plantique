import React from "react";

import Hero from "./components/Hero";
import Purpose from "./components/Purpose";
import Collection from "./components/Collection";
import Offering from "./components/Offering";
import Questions from "./components/Questions";


export default function Index() {
  return (
    <div>
      <Hero />
      <Purpose />
      <Collection />
      <Offering />
      <Questions />
    </div>
  )
}