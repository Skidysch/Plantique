import React, { useState, useEffect } from 'react';

import Header from './components/Header';
import Hero from './components/Hero';
import Purpose from './components/Purpose';
import Collection from './components/Collection';
import Offering from './components/Offering';
import Questions from './components/Questions';
import Footer from './components/Footer';
import MobileHeaderBreakpoint from './components/responsive/MobileHeaderBreakpoint';
import MobileHeader from './components/MobileHeader';
import HeaderBreakpoint from './components/responsive/HeaderBreakpoint';

import './App.css';
import './index.css';

function App() {
  const [scrollOpacity, setScrollOpacity] = useState(0);
  const scrollThreshold = 700;

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    }
  }, []);
  
  const handleScroll = () => {
    const scrollY = window.scrollY;
    if (scrollY <= scrollThreshold) {
      const opacity = scrollY / scrollThreshold;
      setScrollOpacity(opacity);
    } else {
      setScrollOpacity(1);
    }
  }

  return (
    <div className='wrapper'>
      <HeaderBreakpoint>
        <Header handleScroll={handleScroll}
                scrollOpacity={scrollOpacity}
        />
      </HeaderBreakpoint>
      <MobileHeaderBreakpoint>
        <MobileHeader handleScroll={handleScroll}
                scrollOpacity={scrollOpacity}
        />
      </MobileHeaderBreakpoint>
      <Hero />
      <Purpose />
      <Collection />
      <Offering />
      <Questions />
      <Footer />
    </div>
  )
}

export default App
