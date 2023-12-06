import React from "react";
import Breakpoint from "./Breakpoint";

export default function HeaderMobileBreakpoint(props) {
  return (
    <Breakpoint name='headerMobile'>
      {props.children}
    </Breakpoint>
  )
}