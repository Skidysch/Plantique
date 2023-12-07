import React from "react";

export default function GlassPlaceholder(props) {
  const styles = {
    borderRadius: props.radius + "px",
    border: props.hasBorder ? "1px solid #979797" : "none",
  };

  return (
    <div className="glass" style={styles}>
      {props.content}
    </div>
  );
}
