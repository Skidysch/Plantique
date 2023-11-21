import React from "react";
import MediaQuery from 'react-responsive';

const breakpoints = {
  desktopLarge: '(min-width: 1250px)',
  desktop: '(min-width: 992px) and (max-width: 1249px)',
  tabletLarge: '(min-width: 768px) and (max-width: 991px)',
  header: '(min-width: 769px',
  mobileHeader: '(max-width: 768px)',
  tablet: '(min-width: 600px) and (max-width: 767px)',
  phoneLarge: '(min-width: 420px) and (max-width: 599px)',
  phone: '(max-width: 419px)',
}

export default function Breakpoint(props) {
  const breakpoint = breakpoints[props.name] || breakpoints.desktopLarge;
  
  return (
    <MediaQuery {...props} query={breakpoint}>
      {props.children}
    </MediaQuery>
  );
}