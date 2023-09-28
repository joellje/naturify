import React, { useState, useEffect } from "react";

function LandingPage() {
  const SPOTIFY_CLIENT_ID = process.env.REACT_APP_SPOTIFY_CLIENT_ID;
  const REDIRECT_URI = process.env.REACT_APP_REDIRECT_URI;
  const scope = "user-read-private user-read-email";
  const authenticated = localStorage.getItem("accessToken") !== null;

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
    window.location = `https://accounts.spotify.com/authorize?client_id=${SPOTIFY_CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${scope}&response_type=token&show_dialog=true`;
  };

  const handleLogout = () => {
    localStorage.clear();
    window.location.reload();
  };

  return (
    <div className="LandingPage">
      <h1>Landing Page</h1>
      {!authenticated && <button onClick={handleLogin}>Login</button>}
      {authenticated && <button onClick={handleLogout}>Logout</button>}
    </div>
  );
}

export default LandingPage;
