import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import siteBg from "../assets/siteBg.jpeg";

const RegisterForm = (props) => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    first_name: "",
    second_name: "",
    pass_word: "",
    recovery_key: "",
    date_created: new Date().toISOString(),
    email: "",
    address_1: "",
    address_2: "",
    city: "",
    zip: "",
    country: "",
    last_date_updated: new Date().toISOString(),
    error: "",
  });

const handleSubmit = async (e) => {
    e.preventDefault();
    setFormData({ ...formData, error: null });
    let success = true;
    const payload = JSON.stringify(formData);
  
    try {
      const response = await fetch("http://localhost:8000/users/create_user/", {
        method: "POST",
        body: payload,
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      if (!response.ok) {
        const errorText = await response.text();
        console.error(`Error: ${response.status} - ${errorText}`);
        throw new Error(errorText);
      }
  
      const data = await response.json();
  
      if (!success) {
        let errorText = "";
        for (const err in data.errors) {
          for (const msg in data.errors[err]) {
            errorText += data.errors[err][msg];
            
          }
        }
        console.log(errorText);
        setFormData({
          ...formData,
          error: errorText,
        });
      }
      if (data.success) {
        window.sessionStorage.setItem("auth", true);
        window.sessionStorage.setItem("user_id", data.user_id);
        window.sessionStorage.setItem("token", data.token);
    
        console.log("Registration successful! Navigating to login.");
         // Navigate to the login page
    }
    navigate('/login');
    } catch (error) {
      console.error(error);
      setFormData({
        ...formData,
        error: "Error connecting to the server",
        
      });
      
    }
  };
  
  return (
    <div className=" px-36">
      

        {/* Content container */}
        <div className="max-w-[1240px] mx-auto h-full flex flex-col justify-center items-center relative ">
          {/* Welcome heading */}
          <div className="max-w-2xl mx-auto">
            <div className="bg-gradient-to-br from-lime-500 via-yellow-500 to-yellow-300 p-4 rounded-lg shadow-xl pl-3 border border-green-400 rounded-lg max-w-xl p-4 sm:p-6 lg:p-8 flex space-x-4">
              <form className="flex-grow space-y-6 " action="#">
                <div className="flex space-x-4">
                  <div className="flex-1">
                    <label
                      htmlFor="first_name"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      First Name
                    </label>
                    <input
                      type="text"
                      name="first_name"
                      id="first_name"
                      value={formData.first_name}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          first_name: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>

                  <div className="flex-1">
                    <label
                      htmlFor="second_name"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Last Name
                    </label>
                    <input
                      type="text"
                      name="second_name"
                      id="second_name"
                      value={formData.second_name}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          second_name: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                </div>
                <div className="flex space-x-4">
                  <div className="flex-1">
                    <label
                      htmlFor="pass_word"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Email
                    </label>
                    <input
                      type="email"
                      name="email"
                      id="email"
                      value={formData.email}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          email: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                  <div className="flex-1">
                    <label
                      htmlFor="confirm_email"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Confirm Email
                    </label>
                    <input
                      type="email"
                      name="email"
                      id="email"
                      value={formData.email}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          email: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                </div>

                <div className="flex space-x-4">
                  <div className="flex-1">
                    <label
                      htmlFor="pass_word"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Password
                    </label>
                    <input
                      type="password"
                      name="pass_word"
                      id="pass_word"
                      value={formData.pass_word}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          pass_word: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                  <div className="flex-1">
                    <label
                      htmlFor="confirm_password"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Confirm Password
                    </label>
                    <input
                      type="password"
                      name="confirm_password"
                      id="confirm_password"
                      value={formData.confirm_password}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          confirm_password: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                </div>
                <div className="flex space-x-4">
                  <div className="flex-1">
                    <label
                      htmlFor="first_name"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Recovery Key
                    </label>
                    <input
                      type="text"
                      name="recovery_key"
                      id="recovery_key"
                      value={formData.recovery_key}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          recovery_key: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                  <div className="flex-1">
                    <label
                      htmlFor="address_1"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Address Line 1
                    </label>
                    <input
                      type="text"
                      name="address_1"
                      id="address_1"
                      value={formData.address_1}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          address_1: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                </div>
                <div className="flex space-x-4">
                  <div className="flex-1">
                    <label
                      htmlFor="city"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      City
                    </label>
                    <input
                      type="text"
                      name="city"
                      id="city"
                      value={formData.city}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          city: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                  <div className="flex-1">
                    <label
                      htmlFor="address_1"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Address Line 2
                    </label>
                    <input
                      type="text"
                      name="address_2"
                      id="address_2"
                      value={formData.address_2}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          address_2: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                </div>
                <div className="flex space-x-4">
                  <div className="flex-1">
                    <label
                      htmlFor="country"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Country
                    </label>
                    <input
                      type="country"
                      name="country"
                      id="country"
                      value={formData.country}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          country: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                  <div className="flex-1">
                    <label
                      htmlFor="zipcode"
                      className="text-sm font-medium text-gray-900 block mb-2 "
                    >
                      Zip Code
                    </label>
                    <input
                      type="text"
                      name="zip"
                      id="zip"
                      value={formData.zip}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          zip: e.target.value,
                        })
                      }
                      className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-[#32bb6f] focus:border-[#32bb6f] block w-full p-2.5 "
                      required={true}
                    />
                  </div>
                </div>

                <div className="flex space-x-4">{/* ... */}</div>
                <button
                 onClick={(e) => { // Ensure this line is added to prevent the default form submission behavior
                    handleSubmit(e);
                  }}
                  className="w-full text-white bg-[#32bb6f] hover:bg-[#90e8b7] focus:ring-4 focus:ring-[#4fee97] font-medium rounded-lg text-sm px-5 py-2.5 text-center "
                >
                  Register
                </button>
                {/* Display error message */}
                {formData.error && (
                  <p className="text-red-500 text-sm mt-2">{formData.error}</p>
                )}
                <div className="text-sm font-medium text-[#32bb7f] ">
                  Not registered?{" "}
                  <a
                    href={"/register"}
                    className="text-[#32bb6f] hover:underline "
                  >
                    Create account
                  </a>
                </div>
              </form>
            </div>
          </div>
        </div>
      
    </div>
  );
};

export default RegisterForm;
