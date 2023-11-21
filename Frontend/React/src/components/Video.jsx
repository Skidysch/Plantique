import React, {useRef, useState} from "react";
import Button from "./Button";

export default function Video(props) {
  const videoButton = 
  <svg xmlns="http://www.w3.org/2000/svg" width={props.btnSize === 60 ? "24" : "62"} height={props.btnSize === 60 ? "24" : "62"} viewBox="0 0 62 62" fill="none">
    <path d="M45.1825 24.8001L14.4667 43.3226C12.6583 44.4076 10.3333 43.1159 10.3333 40.9976V20.3309C10.3333 11.3151 20.0725 5.6834 27.9 10.1784L39.7575 16.9984L45.1567 20.0984C46.9392 21.1576 46.965 23.7409 45.1825 24.8001Z" fill="white"/>
    <path d="M46.7325 39.9385L36.27 45.9835L25.8333 52.0026C22.0875 54.1468 17.8508 53.7076 14.7767 51.5376C13.2783 50.5043 13.4592 48.2051 15.035 47.2751L47.8692 27.5902C49.4192 26.6602 51.46 27.5385 51.7442 29.321C52.39 33.3252 50.7367 37.6393 46.7325 39.9385Z" fill="white"/>
  </svg>

  const [isPlaying, setIsPlaying] = useState(false);
  const videoRef = useRef(null);

  const togglePlay = () => {
    if (isPlaying) {
      videoRef.current.pause();
    } else {
      videoRef.current.play();
    }
    setIsPlaying(!isPlaying);
  }

  return (
    <div className="video-wrapper">
      <video className="video" width={props.width}
            height={props.height}
            poster={props.poster}
            ref={videoRef}
            controls={isPlaying}
            >
        <source src={props.source} type={props.type}/>
      </video>
      {!isPlaying && (
        <div onClick={togglePlay}>
          <Button content={videoButton}
                  btnRound={true}
                  btnDark={true}
                  size={props.btnSize} />
        </div>
      )}
    </div>
  )
}