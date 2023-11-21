import React from "react";
import Breakpoint from "./Breakpoint";

export default function MobileHeaderBreakpoint(props) {
  return (
    <Breakpoint name='mobileHeader'>
      {props.children}
    </Breakpoint>
  )
}