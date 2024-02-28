import React, { useState, useEffect } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import HeaderMobileBreakpoint from "./components/responsive/HeaderMobileBreakpoint";
import HeaderBreakpoint from "./components/responsive/HeaderBreakpoint";

import "./styles/App.css";
import { Outlet } from "react-router-dom";
import HeaderMobile from "./components/HeaderMobile";
import ScrollToTop from "./components/Scroll";

function App() {
  // TODO: images lazy loading
  const [scrollOpacity, setScrollOpacity] = useState(0);
  const scrollThreshold = 700;

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  const handleScroll = () => {
    const scrollY = window.scrollY;
    if (scrollY <= scrollThreshold) {
      const opacity = scrollY / scrollThreshold;
      setScrollOpacity(opacity);
    } else {
      setScrollOpacity(1);
    }
  };

  return (
    <div className="wrapper">
      <ScrollToTop />
      <HeaderBreakpoint>
        <Header
          handleScroll={handleScroll}
          scrollOpacity={scrollOpacity}
        />
      </HeaderBreakpoint>
      <HeaderMobileBreakpoint>
        <HeaderMobile
          handleScroll={handleScroll}
          scrollOpacity={scrollOpacity}
        />
      </HeaderMobileBreakpoint>
      <main className="main">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
}

export default App;
