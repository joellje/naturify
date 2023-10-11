import React, { useState, useEffect } from "react";

function LandingPage() {
  const SPOTIFY_CLIENT_ID = process.env.REACT_APP_SPOTIFY_CLIENT_ID;
  const REDIRECT_URI = process.env.REACT_APP_REDIRECT_URI;
  const scope =
    "user-read-private user-read-email playlist-modify-public user-modify-playback-state";
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const authenticated = getCookieByName("accessToken") !== null;

  function getCookieByName(cookieName) {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(cookieName + "=")) {
        return cookie.substring(cookieName.length + 1);
      }
    }
    return null;
  }

  function deleteCookie(cookieName) {
    document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
  }

  const handleSearch = async () => {
    setLoading(true);
    const data = {
      access_token: getCookieByName("accessToken"),
      token_type: "Bearer",
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
      const { access_token, expires_in } = getTokenValues(window.location.hash);
      const expirationDate = new Date(
        Date.now() + expires_in * 1000
      ).toUTCString();
      const setCookie = () => {
        document.cookie = `accessToken=${access_token}; expires=${expirationDate}; path=/`;
      };
      setCookie();
      window.location = "http://localhost:3000/";
    }
  });

  const handleLogin = () => {
    setLoading(true);
    window.location = `https://accounts.spotify.com/authorize?client_id=${SPOTIFY_CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${scope}&response_type=token&show_dialog=true`;
  };

  const handleLogout = () => {
    deleteCookie("accessToken");
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
