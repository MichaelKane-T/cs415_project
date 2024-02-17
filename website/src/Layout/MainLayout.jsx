import React from "react";
import Footer from "../Components/Footer";
import Navbar from "../Components/Navbar";

function MainLayout({ children }) {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <div className="flex-grow p-20">{children}</div>
      <Footer />
    </div>
  );
}

export default MainLayout;
