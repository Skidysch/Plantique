import React, {useState} from "react";
import Button from "./Button";
import { ArrowRightDown } from "./SVG";

export default function QuestionCard(props) {

  const [isExpanded, setIsExpanded] = useState(false);

  const toggleQuestion = () => {
    setIsExpanded(!isExpanded);
  }

  const buttonExplandedClass = isExpanded ? "btn--expanded" : ""
  const answerExplandedClass = isExpanded ? "answer--expanded" : ""

  return (
    <div className="question-card">
      <div className="question-card__top" onClick={toggleQuestion}>
        <h4 className="question-card__question">
          {props.question}
        </h4>
        <div className={"question-card__button " + buttonExplandedClass}>
          <Button content={ <ArrowRightDown />}
                  btnRound={true}
                  btnLight={true}
                  size={92} />
        </div>
      </div>
      <div className="question-card__bottom">
        <p className={"question-card__answer " + answerExplandedClass}>
          {props.answer}
        </p>
      </div>
    </div>
  )
}