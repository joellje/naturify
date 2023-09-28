import React, { useState, useEffect } from "react";

function LandingPage() {
  const SPOTIFY_CLIENT_ID = process.env.REACT_APP_SPOTIFY_CLIENT_ID;
  const REDIRECT_URI = process.env.REACT_APP_REDIRECT_URI;
  const scope = "user-read-private user-read-email";
  const authenticated = localStorage.getItem("accessToken") !== null;
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    const data = {
      access_token: localStorage.getItem("accessToken"),
      token_type: localStorage.getItem("tokenType"),
      search_query: searchQuery,
    };
    setSearchQuery("");

    const queryResponse = await fetch(`http://localhost:5000/query`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const queryResponseJSON = await queryResponse.json();
    console.log(queryResponseJSON);
    setLoading(false);
  };

  const getTokenValues = (hash) => {
    const stringAfterHashtag = hash.substring(1);
    const paramsInUrl = stringAfterHashtag.split("&");
    const tokenValues = paramsInUrl.reduce((mapping, mappingString) => {
      const [key, value] = mappingString.split("=");
      mapping[key] = value;
      return mapping;
    }, {});

    return tokenValues;
  };

  useEffect(() => {
    if (window.location.hash) {
      const { access_token, expires_in, token_type } = getTokenValues(
        window.location.hash
      );

      localStorage.clear();

      localStorage.setItem("accessToken", access_token);
      localStorage.setItem("tokenType", token_type);
      localStorage.setItem("expiresIn", expires_in);
      window.location = "http://localhost:3000/";
    }
  });

  const handleLogin = () => {
    setLoading(true);
    window.location = `https://accounts.spotify.com/authorize?client_id=${SPOTIFY_CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${scope}&response_type=token&show_dialog=true`;
  };

  const handleLogout = () => {
    localStorage.clear();
    window.location.reload();
  };

  return (
    <div className="LandingPage">
      <h1>Landing Page</h1>
      {!authenticated && (
        <button
          className={`btn btn-primary ${loading === true ? "loading" : " "}`}
          onClick={handleLogin}
        >
          Login
        </button>
      )}
      {authenticated && (
        <div className="relative text-gray-600">
          <input
            type="text"
            className="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
            placeholder="Search..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <button
            type="submit"
            className={`btn btn-primary ${loading === true ? "loading" : " "}`}
            onClick={handleSearch}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-4 w-4 text-black-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M21 21l-4.35-4.35"
              />
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M15 11a4 4 0 11-8 0 4 4 0 018 0z"
              />
            </svg>
          </button>
        </div>
      )}
      {authenticated && (
        <button
          className={`btn btn-primary ${loading === true ? "loading" : " "}`}
          onClick={handleLogout}
        >
          Logout
        </button>
      )}
    </div>
  );
}

export default LandingPage;
