import React, { useEffect, useState } from 'react'
import "./Slide.scss"
import Slider from 'infinite-react-carousel';
import Card from '../card/Card';
import { cards } from '../../data';


  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://192.168.178.25:5001/');
      const jsonData = await response.json();
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

const Slide = () => {
    console.log(cards)



  return (
    <div className='slide'>
        <div className="container">
        <Slider arrowsScroll={2} slidesPerRow={2} slidesToShow={3} >
            {data.map(card=>(
                <Card item={card} key={card.id}/>
            ))}
        </Slider>
        </div>
    </div>
  )
}


export default Slide