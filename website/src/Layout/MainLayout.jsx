import React from "react";
import Footer from "../Components/Footer";
import Navbar from "../Components/Navbar";

function MainLayout({ children }) {
  return (
    <div>
      <Navbar />
      <div>{children}</div>
      <Footer />
    </div>
  );
}

export default MainLayout;
