import "./App.css";
import LandingPage from "./pages/LandingPage";
import HomePage from "./pages/HomePage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />}></Route>
        <Route path="/home" element={<HomePage />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
