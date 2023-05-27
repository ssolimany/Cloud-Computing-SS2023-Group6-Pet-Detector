import React, { useEffect, useState } from 'react'
import "./Navbar.scss"
// import logo from "./assets/images/cat1.jpg"

const Navbar = () => {

  const [active, setActive] = useState(false);

  const isActive = ()=>{
    window.scrollY > 0 ? setActive(true) : setActive(false)
  }

  useEffect(()=>{
    window.addEventListener("scroll", isActive );
    return ()=>{
        window.removeEventListener("scroll", isActive);
    }
  },[])
  
  return (
    <div className={active ? "navbar active" : "navbar"}>
        <div className="container">
            <div className="applogo">
                <img src="./logo/pdlogo.png" alt="AppLogo" />
                <span>Pet Detection</span>
            </div>

            <div className="frauaslogo">
                <img src="./logo/frauaslogo.png" alt="fra-uas" />
            </div>
            <div className="about us">
                <span>About us</span>
            </div>
            <div className="signin">
                <button>Sign In</button>
            </div>
        </div>
        { active && (
            <><hr />
            <div className="menu">
                <span>All</span>
                <span>Cat</span>
                <span>Dog</span>
                <span>Golden Hamster</span>
            </div>
            </>
        )}
    </div>
  )
}

export default Navbar