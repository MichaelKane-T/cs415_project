import { useState } from "react";
import { Link } from 'react-router-dom';
import logo from "../assets/logo.png";

const navItems = ["Home", "User Profile", "Module1", "Module2"];
const navRoutes = ["/",  "/user-profile", "/module1", "/module2"];

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <div className="fixed z-50 top-0 w-full bg-white">
        <nav className="container flex justify-center items-center z-20 py-6">
          <div className="hidden lg:block gap-4 text-md  text-lime-600">
            {navItems.map((navItem, index) => (
              <Link
              className="mx-3 py-5 hover:animate-jump-out "
                key={navItem}
                to={navRoutes[index]}
                
              >
                {navItem}
              </Link>
            ))}
          </div>

         

          <button
            onClick={() => setIsOpen(!isOpen)}
            className="lg:hidden focus:outline-none"
          >
            <img
              className={`${isOpen && "hidden"}`}
              src="/icons/icon-hamburger.svg"
              alt=""
            />
            <img
              className={isOpen ? "block" : "hidden"}
              src="/icons/icon-close.svg"
              alt=""
            />
          </button>
        </nav>
      </div>

      {/* Modal */}
      <div
        className={`fixed inset-0 z-30 bg-gray-800 bg-opacity-50 ${isOpen ? "block" : "hidden"}`}
      >
        <div className="flex items-center justify-center gap-2 bg-white text-primary-dark-blue flex-col text-center mx-5 my-20 py-4 rounded">
          {navItems.map((navItem, index) => (
            <Link key={navItem} to={navRoutes[index]} className="py-2 hover:animate-jump-out">
              {navItem}
            </Link>
          ))}
        </div>
      </div>
    </>
  );
}
