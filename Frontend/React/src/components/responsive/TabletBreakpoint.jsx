import React from "react";
import Breakpoint from "./Breakpoint";

export default function TabletBreakpoint(props) {
  return (
    <Breakpoint name='tablet'>
      {props.children}
    </Breakpoint>
  )
}