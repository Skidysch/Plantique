import React, { useState } from "react";
import Button from "./Button";
import { ArrowRightPlant, Heart} from "./SVG";
import { Link } from "react-router-dom";

export default function PlantCard(props) {
  const [isLiked, setIsLiked] = useState(false);

  const toggleHeart = () => {
    setIsLiked(!isLiked);
  }

  return (
    <div className="plant-card">
      <div className="plant-card__cover">
        <Link className="plant-card__link" to={props.link}>
          <img className="plant-card__image" src={props.image_url} alt="Plant card Image"/>
        </Link>
        <div className="plant-card__like-button" onClick={toggleHeart}>
          <Button content={<Heart liked={isLiked}/>}
                  btnLike={true}
                  btnRound={true}
                  size={60} />
        </div>
      </div>
      <div className="plant-card__bottom">
        <div className="plant-card__info">
          <Link className="plant-card__title" to={props.link}>
            <h4>{props.name}</h4>
          </Link>
          <p className="plant-card__soil">Soil type: {props.soil_type}</p>
          <p className="plant-card__price">$ {props.price}</p>
        </div>
        <div className="plant-card__button">
          <Link to={props.link}>
            <Button content={<ArrowRightPlant />}
                    btnDark={true}
                    btnRound={true}
                    size={60}/>
          </Link>
        </div>
      </div>
    </div>
  )
}