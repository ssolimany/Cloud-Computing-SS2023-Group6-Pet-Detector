import React from 'react'
import "./Footer.scss"

const Footer = () => {
  return (
    <div className='footer'>
      <div className="container">
        <div className="top">
          <div className="left">
            <h2>Infos</h2>
            <span>Cloud Computing</span>
            <span>Summer Term 2023</span>
            <span>Gruppe 6</span>
          </div>
          <div className="center">
            <h2>Supervisor</h2>
            <span>Prof. Dr. Christian Baun</span>
          </div>
          <div className="right">
            <h2>Notions</h2>
            <span>Edge Computing</span>
            <span>Distributed Systems</span>
            <span>Containarization</span>
          </div>
        </div>
        <hr/>
        <div className="bottom">
          <div className="left">
            <span>© Pet Detection International Ltd. 2023</span>
          </div>
          <div className="right">
            <div className="social">
              <img src="/logo/twitter.png" alt="" />
              <img src="/logo/facebook.png" alt="" />
              <img src="/logo/linkedin.png" alt="" />
              <img src="/logo/pinterest.png" alt="" />
              <img src="/logo/instagram.png" alt="" />

           </div>
          </div>
        </div>
      
      </div>

    </div>
  )
}

export default Footer