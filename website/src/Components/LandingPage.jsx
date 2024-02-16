import React from "react";
import userImage from "../assets/userImage.jpeg";
import { useNavigate } from "react-router";

function Hero() {
  const backgroundImageStyle = {
    backgroundImage: `url(${userImage})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
  };
  //function to handle button on click
  const navigate = useNavigate();
  const handleButtonClick = () => {
    //navigate to about page
    navigate("/login");
  };

  return (
    <div className="text-white px-8">
      {/* Full-page background image */}
      <div className="w-screen h-screen overflow-hidden relative" style={backgroundImageStyle}>
        {/* Dark overlay to enhance text visibility */}
        <div className="absolute inset-0 bg-black opacity-50"></div>

        {/* Content container */}
        <div className="max-w-[1240px] mx-auto h-full flex flex-col justify-center items-center relative z-10">
          {/* Welcome heading */}
          <h1 className="text-5xl font-bold mb-6 animate-bounce animate-delay-300 ">Welcome to Fantasy Football</h1>

          {/* Login button */}
          <button
            onClick={handleButtonClick}
            className="text-white w-[200px] rounded-md font-medium my-6 mx-auto py-3  bg-[#32bb6f] transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 hover:bg-[#77dfa6] duration-300"
          >
            Login
          </button>
          <a href={"/register"}><p className=" text-center text-[#32bb6f] block">Sign up?</p></a>
        </div>
      </div>
    </div>
  );
}

export default Hero;
