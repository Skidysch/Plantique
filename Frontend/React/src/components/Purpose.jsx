import React from "react";
import Video from "./Video";
import Poster from "/purpose-poster.jpg";
import VideoSource from "/purpose-video.mp4";
import healthyIcon from "/healthy-icon.png";

export default function Purpose() {
  return (
    <div className="purpose">
      <div className="purpose__header">
        <h1 className="purpose__title">Plants for the People</h1>
        <p className="purpose__text">
          We want our Visitors to be inspire to get their hands dirty
        </p>
      </div>
      <Video
        width={244}
        height={142}
        poster={Poster}
        source={VideoSource}
        type="video/mp4"
        btnSize={60}
      />
      <div className="purpose__description">
        <p>
          Each plant is cared{" "}
          <img className="purpose__image" src={healthyIcon} /> for by our
          <br />
          horticultural experts, so they are as
          <br />
          happy as healthy as they get.
        </p>
      </div>
    </div>
  );
}
