import React, { useState } from "react";

export default function Button(props) {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const hoverClass = isHovered ? "btn--hovered " : "";

  return (
    <button
      className={
        "btn " +
        hoverClass +
        (props.btnLarge ? "btn--large " : "") +
        (props.btnHeader ? "btn--header " : "") +
        (props.btnLight ? "btn--light " : "") +
        (props.btnDark ? "btn--dark " : "") +
        (props.btnLike ? "btn--like " : "") +
        (props.btnRound
          ? "btn--round " +
            (props.size === 60
              ? "btn--60 "
              : props.size === 92
              ? "btn--92 "
              : "btn--172 ")
          : "") +
        (props.disabled ? "disabled " : "")
      }
      type={props.type}
      onClick={props.onClick}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      disabled={props.disabled}
    >
      {props.content}
    </button>
  );
}
