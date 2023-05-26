import React from 'react'
import "./Card.scss"

const Card = ({item}) => {
  return (
    <div className='card'>
       <img src={`./img/${item.imagePath}`} alt="imagePath"/>
       <span className="pettype">{item.petType}</span>
       <span className="timeStamp">{new Date(item.timeStamp).toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric', hour12: true })}</span>
       <span className='confidence'>Confidence: {item.confidence}</span>
       <span className='detection'>Setection: {item.detection}</span>
    </div>
  )
}

export default Card