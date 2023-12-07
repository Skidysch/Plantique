import React from "react";
import Breakpoint from "./Breakpoint";

export default function HeaderBreakpoint(props) {
  return <Breakpoint name="header">{props.children}</Breakpoint>;
}
