import React from 'react'
import "./Card.scss"

const Card = ({item}) => {
  const formattedTimestamp = item.timestamp ? formatTimestamp(item.timestamp) : "";
  return (
    <div className='card'>
       <img src={`data:image/jpeg;base64, ${item.image_data}`} alt="imagePath"/>
       <span className="pettype">{item.detection_classes}</span>
       <span className="timeStamp">{formattedTimestamp}</span>
       <span className='confidence'>Confidence: {item.detection_confidence_values}</span>
       <span className='detection'>Detection: {item.detection_amount}</span>
    </div>
  )
}
function formatTimestamp(timestamp) {
  const year = timestamp.slice(0, 4);
  const month = timestamp.slice(4, 6);
  const day = timestamp.slice(6, 8);
  const hour = timestamp.slice(8, 10);
  const minute = timestamp.slice(10, 12);
  const second = timestamp.slice(12, 14);

  return `${year}-${month}-${day} ${hour}:${minute}:${second}`;
}

export default Card