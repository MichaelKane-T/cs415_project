import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const UserProfile = () => {
  const navigate = useNavigate();
  const [userColumns, setUserColumns] = useState([]);
  const [record, setRecord] = useState([]);
  const [addressColumns, setAddressColumns] = useState([]);
  const [addresses, setAddresses] = useState([]);
  const [phoneColumns, setPhoneColumns] = useState([]);
  const [phones, setPhones] = useState([]);
  const [infoColumns, setInfoColumns] = useState([]);
  const [info, setInfo] = useState([]);
  const user_id = window.sessionStorage.getItem('user_id');

  useEffect(() => {
    if (!window.sessionStorage.getItem('auth')) navigate('/unauthorized');

    fetch('http://localhost:8000/users/user/' + user_id)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);

        if (data.user) {
          setUserColumns(Object.keys(data.user));
          setRecord(data.user);
        }

        if (data.info && data.info.length > 0) {
          setInfoColumns(Object.keys(data.info[0]));
          setInfo(data.info);
        }
      })
      .catch((error) => console.error(error));
  }, [navigate, user_id]);

  useEffect(() => {
    if (!window.sessionStorage.getItem('auth')) navigate('/unauthorized');

    fetch('http://localhost:8000/addresses/user/' + user_id)
      .then((res) => res.json())
      .then((data) => {
        console.log("......................");
        console.log(data);
        console.log("......................");

        if (data.useraddress) {
          setAddressColumns(Object.keys(data.useraddress));
          setRecord(data.useraddress);
        }

        if (data.useraddress && data.useraddress.length > 0) {
          setAddressColumns(Object.keys(data.useraddress[0]));
          setAddresses(data.useraddress);
          console.log(data.useraddress);
        }
      })
      .catch((error) => console.error(error));
  }, [navigate, user_id]);

  function handleLogout(e) {
    e.preventDefault();
    window.sessionStorage.removeItem('auth');
    window.sessionStorage.removeItem('user_id');
    window.sessionStorage.removeItem('token');
    navigate('/login');
  }

  const Card = ({ title, data }) => {
    return (
      <div className="max-w-[1240px] mx-auto h-full flex flex-col justify-center items-center relative z-10">
        <h2 className="text-xl font-bold mb-4">{title}</h2>
        <div className="flex grid-flow-row md:grid-flow-row lg:grid-flow-row gap-4">
          {data.map((item, i) => (
            <div
              key={`${title.toLowerCase()}-card-${i}`}
              className="bg-gradient-to-br from-lime-500 via-yellow-500 to-yellow-300 p-4 rounded-lg shadow-xl pl-3 hover:scale-105 duration-300 border border-green-400"
            >
              {Object.keys(item).map((key, j) => (
                <div key={`${title.toLowerCase()}-card-${i}-${j}`} className="mb-2">
                  <p className="font-bold text-black">{key.replaceAll('_', ' ').toUpperCase()}</p>
                  {/* Check if the value is an object or array, and handle it accordingly */}
                  {typeof item[key] === 'object' ? (
                    // If it's an object or array, convert it to a string for display
                    <p className="text-black">{JSON.stringify(item[key])}</p>
                  ) : (
                    // If it's a primitive type, display it directly
                    <p className="text-black">{item[key]}</p>
                  )}
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    );
  };
  

  return (
    <div className="text-white px-8">
      <div className="w-screen h-screen overflow-hidden relative">
        <div className="absolute inset-0 bg-black opacity-50"></div>

        <div className="max-w-[1240px] mx-auto h-full flex flex-col justify-center items-center relative z-10">
          <div className="flex flex-col md:flex-row justify-items-end gap-4">
            <div className="flex row-span-1">
              <Card title="User Info" data={info} />
            </div>
            <div className="flex row-span-1">
              <Card title="Addresses" data={addresses} />
              {/* Add the button at the bottom */}
              
            </div>
            {/* <div className="col-span-1">
              <Card title="Phones" data={phones} />
            </div> */}
          </div>
          <button
                className="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                onClick={handleLogout}
                key="logout-button"
              >
                Logout
              </button>
        </div>
      </div>
    </div>
  );
};


export default UserProfile;
