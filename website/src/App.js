import React from "react";
import { BrowserRouter as Router,
          Routes,
          Route,
          Link} from "react-router-dom";
import './App.css';
import RegisterForm from "./Components/RegisterForm";
import LoginForm from "./Components/LoginForm";
import LandingPage from "./Components/LandingPage";
import UserProfile from "./Components/UserProfile";
import UserView from "./Components/UserView";
import Module1 from "./Components/Module1";
import Module2 from "./Components/Module2";
import Module3 from "./Components/Module3";
import MainLayout from './Layout/MainLayout';


function NoMatch() {
  return (
    <div style={{ padding: 20 }}>
      <h2>404: Page Not Found</h2>
      <p><font color="white">There is no page at the requested url</font></p>
    </div>
  );
}

function UnAuthorized() {
  return (
    <div style={{ padding: 20 }}>
      <h2>401: Unauthorized</h2>
      <p><font color="white">You are not authorized to view the page at the requested url</font></p>
    </div>
  );
}

function App() {

  return (
      <MainLayout>
       <div className="App">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/register" element={<RegisterForm />} />
            <Route path="/userprofile" element={<UserProfile />} />
            <Route path="/users" element={<UserView />} />
            <Route path="/modules/1" element={<Module1 />} />
            <Route path="/modules/2" element={<Module2 />} />
            <Route path="/modules/3" element={<Module3 />} />
            <Route path="/unauthorized" element={<UnAuthorized />} />
            <Route path="*" element={<NoMatch />} />
          </Routes>
          </div>

      </MainLayout>
  );
}

export default App;
