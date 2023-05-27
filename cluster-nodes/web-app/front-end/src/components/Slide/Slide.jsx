import React, { useEffect, useState } from 'react'
import "./Slide.scss"
import Slider from 'infinite-react-carousel';
import Card from '../card/Card';
import { cards } from '../../data';




const Slide = () => {
const [data, setData] = useState(null);

useEffect(() => {
  fetchData();
}, []);

const fetchData = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5001/');
    const jsonData = await response.json();
    setData(jsonData);
  } catch (error) {
    console.error('Error fetching DATA:', error);
  }
};
  console.log("hiiiiiiiiiiii")
  console.log(data)

  const items =  data ?? cards
  return (
    <div className='slide'>
        <div className="container">
        <Slider arrowsScroll={2} slidesPerRow={1} slidesToShow={3} >
            {items.map(card=>(
                <Card item={card} key={card.id}/>
            ))}
        </Slider>
        </div>
    </div>
  )
}


export default Slide