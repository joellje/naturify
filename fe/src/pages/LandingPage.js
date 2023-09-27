import React, { useState } from "react";

function LandingPage() {
  const [loading, setLoading] = useState(false);

  const handleLogin = async (event) => {
    event.preventDefault();
    window.location.replace("http://localhost:5000/login");
  };

  return (
    <div className="LandingPage">
      <h1>Landing Page</h1>
      <button
        className={`btn btn-primary ${loading === true ? "loading" : " "}`}
        onClick={handleLogin}
      >
        Login
      </button>
    </div>
  );
}

export default LandingPage;
