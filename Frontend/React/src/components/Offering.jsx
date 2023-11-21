import React from "react";
import Video from "./Video";

export default function Offering() {
  return (
    <div className="offering">
      <div className="offering__header">
        <h2 className="offering__title">
          Quality Plants and Curated Goods
        </h2>
        <p className="offering__description">
          We offer a carefully curated selection of indoor and outdoor plants, hand crafted home goods that put quality ahead of quantity, and living art made right here in the shop: terrariums, landscapes, arrangements, vessels, and holders.
        </p>
      </div>
      <Video width={800} 
             height={470}
             poster='/offering-poster.png'
             source='/offering-video.mp4'
             type='video/mp4'
             btnSize={172} />
    </div>
  )
}