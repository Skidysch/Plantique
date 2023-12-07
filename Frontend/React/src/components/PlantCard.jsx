import React, { useState } from "react";
import Button from "./Button";
import { ArrowRightPlant, Heart} from "./SVG";

export default function PlantCard(props) {
  const [isLiked, setIsLiked] = useState(false);

  const toggleHeart = () => {
    setIsLiked(!isLiked);
  }

  return (
    <div className="plant-card">
      <div className="plant-card__cover">
        <a className="plant-card__link" href="#">
          <img className="plant-card__image" src={props.cover} alt="Plant card Image"/>
        </a>
        <div className="plant-card__like-button" onClick={toggleHeart}>
          <Button content={<Heart liked={isLiked}/>}
                  btnLike={true}
                  btnRound={true}
                  size={60} />
        </div>
      </div>
      <div className="plant-card__bottom">
        <div className="plant-card__info">
          <a className="plant-card__title" href="#">
            <h4>{props.title}</h4>
          </a>
          <p className="plant-card__soil">{props.soil}</p>
          <p className="plant-card__price">{props.price}</p>
        </div>
        <div className="plant-card__button">
          <a href="#">
            <Button content={<ArrowRightPlant />}
                    btnDark={true}
                    btnRound={true}
                    size={60}/>
          </a>
        </div>
      </div>
    </div>
  )
}